# -*- coding: utf-8 -*-


class OpenApi:
    OPENAPI = "openapi"
    INFO = "info"
    TAGS = "tags"
    PATHS = "paths"


class Info:
    TITLE = "title"
    DESCRIPTION = "description"
    VERSION = "version"


class Tags:
    NAME = "name"


class Path:
    SUMMARY = "summary"
    X_FOLDER = "x-apifox-folder"
    X_STATUS = "x-apifox-status"
    DEPRECATED = "deprecated"
    DESCRIPTION = "description"
    TAGS = "tags"
    PARAMETERS = "parameters"
    REQUESTBODY = "requestBody"
    RESPONSES = "responses"


class Parameters:
    NAME = "name"
    IN = "in"
    DESCRIPTION = "description"
    REQUIRED = "required"
    EXAMPLES = "examples"
    SCHEMA = "schema"


class RequestBody:
    CONTENT = "content"
    EXAMPLES = "examples"


class Responses:
    DESCRIPTION = "description"
    CONTENT = "content"
    EXAMPLES = "examples"


class Content:
    SCHEMA = "schema"


class Examples:
    SUMMARY = "summary"
    VAULE = "value"


class Schema:
    TYPE = "type"
    PROPERTIES = "properties"
    REQUIRED = "required"
    X_STATUS = "x-apifox-status"
    X_PROPERTIES = "x-apifox-ignore-properties"


class Properties:
    TYPE = "type"
    TITLE = "title"
    ITEM = "item"
    DESCRIPTION = "description"


class Item:
    TYPE = "type"
    PROPERTIES = "properties"
