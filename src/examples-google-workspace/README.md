# examples-google-workspace

[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)

Although it is not a web site, it is an example of a client that operates Google Workspace.

## More document

- https://developers.google.com/workspace?hl=ja
- https://googleapis.dev/python/google-auth/latest/index.html
- https://docs.gspread.org/en/latest/index.html


## Getting started

Move to this folder:

```shell
cd examples-google-workspace
```

Install dependency packages and install myself locally as editable:

```shell
pdm install
```

Run the command:

```shell
examples-google-cli -h
```


## Configure Google Cloud API

Goto google cloud platforms site:

- https://console.cloud.google.com/welcome

### Enable APIs

1. APIs & Services > Library
2. Enable [Google Drive API] and [Google Sheets API]

### When use service account (silent login).

1. IAM and Admin > Service Accounts > CREATE SERVICE ACCOUNT
   > - Service account details:  
   >   Input service account id.
   > - Grant this service account access to project:  
   >   Select Editor role.
   > - DONE
2. select created service account
3. service account > KEYS > ADD KEY(Create new key)
   > - type(JSON) > Create
4. json file will be downloaded automatically.
5. Rename the file to `service_account.json` and add it to your project
6. _Grant permissions for Google services to service accounts_

### When use user account (OAUTH login).

1. APIs & Services > OAuth consent screen
   > - User type: External > create
   > - OAuth consent screen:
   >   - App name: any name
   >   - User support email: your email
   >   - Email addresses: your email
   > - Test user:
   >   - ADD USERS: your email.
2. Credentials > CREATE CREDENTIALS > OAuth client ID
   > - Select Application Type: Desktop app
   > - CREATE
3. Download json file.
4. Rename the file to `credentials.json` and add it to your project


## How the project was initialized

This project was initialized with the following command:

```shell
pdm init -p src/examples-google-workspace --dist -n
cd src/examples-google-workspace
pdm add -d flake8 mypy black isort pytest-cov pyclean

pdm add pyyaml
pdm add google-api-python-client google-auth-httplib2 google-auth-oauthlib
pdm add google-apps-chat

pdm add -d types-PyYAML

```
# spell-checker:words pyyaml
# spell-checker:words httplib
# spell-checker:words oauthlib

