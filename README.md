# api

[![Build Status](https://github.com/pingview/api/workflows/ci/badge.svg?branch=main&event=push)](https://github.com/pingview/api/actions?query=workflow%3Aci)
[![codecov](https://codecov.io/gh/pingview/api/branch/main/graph/badge.svg?token=7AdYmCx3Go)](https://codecov.io/gh/pingview/api)
[![License](https://img.shields.io/github/license/pingview/api.svg?color=brightgreen)](https://github.com/pingview/api/blob/main/LICENSE)
[![Tag](https://img.shields.io/github/tag/pingview/api.svg?color=brightgreen)](https://github.com/pingview/api/tags)



## Introduction

*api* is a Gerrit API generator of *[pingview](https://github.com/pingview/)* written in Python.



## Prerequisites

- Python >= 3.10.0



## Run

```bash
python api.py --config-file api/config/config.yml --output-file output.json
```



## Usage

```
usage: api.py [-h] --config-file CONFIG_FILE --output-file OUTPUT_FILE [-v]

PingView API

options:
  -h, --help            show this help message and exit
  --config-file CONFIG_FILE
                        config file (.yml)
  --output-file OUTPUT_FILE
                        output file (.json|.yml)
  -v, --version         show program's version number and exit
```



## Settings

*api* parameters can be set in the directory [config](https://github.com/pingview/api/blob/main/api/config).

An example of configuration in [config.yml](https://github.com/pingview/api/blob/main/api/config/config.yml):

```yaml
apiVersion: v1
kind: api
metadata:
  name: api
spec:
  host: https://gerrit-googlesource.g.globit.com/gerrit/+/refs/tags/v3.5.1/Documentation
  index:
    - name: access
      page: rest-api-access.txt
    - name: accounts
      page: rest-api-accounts.txt
    - name: changes
      page: rest-api-changes.txt
    - name: config
      page: rest-api-config.txt
    - name: Documentation
      page: rest-api-documentation.txt
    - name: groups
      page: rest-api-groups.txt
    - name: plugins
      page: rest-api-plugins.txt
    - name: projects
      page: rest-api-projects.txt
```



## License

Project License can be found [here](LICENSE).



## Reference

- [gerrit-api](https://gerrit-googlesource.g.globit.com/gerrit/+/refs/tags/v3.5.1/Documentation/)
- [openapis-spec](https://spec.openapis.org/oas/latest.html)
