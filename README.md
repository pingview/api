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
  host: https://gerrit-documentation.storage.googleapis.com/Documentation/3.5.1
  index:
    - name: access
      page: rest-api-access.html
    - name: accounts
      page: rest-api-accounts.html
    - name: changes
      page: rest-api-changes.html
    - name: config
      page: rest-api-config.html
    - name: groups
      page: rest-api-groups.html
    - name: plugins
      page: rest-api-plugins.html
    - name: projects
      page: rest-api-projects.html
    - name: Documentation
      page: rest-api-documentation.html
```



## License

Project License can be found [here](LICENSE).



## Reference

- [gerrit-api](https://gerrit-documentation.storage.googleapis.com/Documentation/3.5.1/rest-api.html)
- [openapis-spec](https://spec.openapis.org/oas/latest.html)
