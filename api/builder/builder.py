# -*- coding: utf-8 -*-
import json

from api.config.config import ConfigFile, Spec, Index

types = {
    "bool": "boolean",
    "dict": "object",
    "int": "integer",
    "list": "array",
    "str": "string",
}


class BuilderException(Exception):
    def __init__(self, info):
        super().__init__(self)
        self._info = info

    def __str__(self):
        return self._info


class Builder(object):
    def __init__(self, config=None):
        if config is None:
            raise BuilderException("config invalid")
        spec = config.config_file[ConfigFile.SPEC]
        self._index = spec[Spec.INDEX]

    def run(self, data):
        buf = data.splitlines()
        ret = {}
        for item in self._index:
            p = self._parse(buf[item[Index.NAME]])
            ret[item[Index.NAME]] = self._build(buf[item[Index.NAME]], p)
        return self._append(ret)

    def _parse(self, data):
        def _path_helper(data):
            buf = {}
            for i in range(len(data)):
                b = data[i].strip()
                if len(b) != 0 and b.split()[0] == "=":
                    buf = {"name": {"start": i, "end": i + 1}}
                    break
            return buf

        def _endpoints_helper(data):
            buf = []
            for i in range(len(data)):
                b = data[i].strip()
                if len(b) != 0 and b.split()[0] == "==" and b.endswith("Endpoints"):
                    buf.append({"name": {"start": i, "end": i + 1}})
            return buf

        def _name_helper(data, start, end):
            d = {"start": 0, "end": 0}
            s = start
            for i in range(start, end):
                b = data[i].strip()
                if len(b) != 0 and b.split()[0] == "===":
                    d = {"start": i, "end": i + 1}
                    s = i + 1
                    break
            i = s
            s = 0
            e = 0
            while i < end:
                b = data[i].strip()
                if len(b) != 0 and b == "--":
                    if s == 0:
                        s = i + 1
                    else:
                        e = i
                i = i + 1
            n = {"start": s, "end": e}
            return d, n

        def _request_helper(data, start, end):
            s = start
            for i in range(start, end):
                b = data[i].strip()
                if len(b) != 0 and b == ".Request":
                    s = i + 1
                    break
            i = s
            s = 0
            e = 0
            while i < end:
                b = data[i].strip()
                if len(b) != 0 and b == "----":
                    if s == 0:
                        s = i + 1
                        i = i + 1
                        continue
                    if s > 0:
                        e = i
                        break
                i = i + 1
            return {"start": s, "end": e}

        def _response_helper(data, start, end):
            s = start
            for i in range(start, end):
                b = data[i].strip()
                if len(b) != 0 and b == ".Response":
                    s = i + 1
                    break
            i = s
            s = 0
            e = 0
            while i < end:
                b = data[i].strip()
                if len(b) != 0 and b == "----":
                    if s == 0:
                        s = i + 1
                        i = i + 1
                        continue
                    if s > 0:
                        e = i
                        break
                i = i + 1
            return {"start": s, "end": e}

        def _apis_helper(data, start, end):
            buf = []
            s = start
            while s < end:
                description, name = _name_helper(data, s, end)
                if name["start"] == 0 and name["end"] == 0:
                    break
                request = _request_helper(data, s, end)
                response = _response_helper(data, s, end)
                buf.append(
                    {
                        "description": description,
                        "name": name,
                        "request": request,
                        "response": response,
                    }
                )
                s = response["end"]
            return buf

        buf = {"path": _path_helper(data), "endpoints": _endpoints_helper(data)}
        for i in range(len(buf["endpoints"])):
            start = buf["endpoints"][i]["name"]["start"]
            end = (
                buf["endpoints"][i + 1]["name"]["start"]
                if i < len(buf["endpoints"]) - 1
                else len(data)
            )
            buf["endpoints"][i]["apis"] = _apis_helper(data, start, end)

        return buf

    def _build(self, data, parser):
        def _reflect_helper(data):
            buf = {"type": types[type(data).__name__]}
            if isinstance(data, dict):
                prop = {}
                for key, val in data.items():
                    prop[key] = _reflect_helper(val)
                buf["properties"] = prop
                buf["required"] = []
                buf["x-apifox-orders"] = []
                buf["x-apifox-ignore-properties"] = []
            return buf

        def _properties_helper(data, parser, _type):
            s = 0
            for i in range(parser[_type]["start"], parser[_type]["end"]):
                if len(data[i].strip()) == 0:
                    if data[i + 1].strip() == ")]}'":
                        s = i + 2
                    elif data[i + 1].strip() == "{":
                        s = i + 1
                    break
            buf = json.loads("".join(data[s : parser[_type]["end"]]))
            prop = {}
            for key, val in buf.items():
                prop[key] = _reflect_helper(val)
            return prop

        def _example_helper(data, parser):
            s = 0
            for i in range(parser["response"]["start"], parser["response"]["end"]):
                if data[i].strip() == ")]}'":
                    s = i + 1
                    break
            return json.loads("".join(data[s : parser["response"]["end"]]))

        def _responses_helper(data, parser):
            return {
                "200": {
                    "description": "成功",
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "properties": _properties_helper(
                                    data, parser, "response"
                                ),
                                "required": [],
                                "x-apifox-orders": [],
                                "x-apifox-ignore-properties": [],
                            },
                            "examples": {
                                "1": {
                                    "summary": "成功示例",
                                    "value": _example_helper(data, parser),
                                }
                            },
                        }
                    },
                }
            }

        def _request_helper(data, parser):
            return {
                "content": {
                    "application/json": {
                        "schema": {
                            "type": "object",
                            "properties": _properties_helper(data, parser, "request"),
                            "required": [],
                            "x-apifox-orders": [],
                            "x-apifox-ignore-properties": [],
                        }
                    }
                }
            }

        def _param_helper(data, parser):
            # TODO
            return [
                {
                    "name": "Content-Type",
                    "in": "header",
                    "description": "",
                    "required": False,
                    "example": "application/json",
                    "schema": {"type": "string"},
                }
            ]

        def _api_helper(data, path, parser):
            op = data[parser["name"]["start"]].split()[0].lstrip("'").strip().lower()
            api = data[parser["name"]["start"]].split()[1].rstrip("'").strip()
            description = (
                data[parser["description"]["start"]].replace("===", "").strip()
            )
            return {
                api: {
                    op: {
                        "summary": path,
                        "x-apifox-folder": path.lstrip("/"),
                        "x-apifox-status": "developing",
                        "deprecated": False,
                        "description": description,
                        "tags": [path.lstrip("/")],
                        "parameters": _param_helper(data, parser),
                        "requestBody": _request_helper(data, parser),
                        "responses": _responses_helper(data, parser),
                    }
                }
            }

        buf = {}
        path = data[parser["path"]["name"]["start"]].split()[-3].rstrip("/").strip()
        for ep in parser["endpoints"]:
            for api in ep["apis"]:
                b = _api_helper(data, path, api)
                buf = buf | b

        return buf

    def _append(self, data):
        def _helper(data):
            buf = {}
            for _, val in data.items():
                buf = buf | val
            return buf

        tags = []
        paths = _helper(data)
        return {
            "openapi": "3.0.1",
            "info": {
                "title": "gerrit-openapi",
                "description": "Gerrit OpenAPI",
                "version": "3.5.1",
            },
            "tags": tags,
            "paths": paths,
            "components": {"schemas": {}},
        }
