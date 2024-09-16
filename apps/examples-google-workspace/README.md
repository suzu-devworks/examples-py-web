# examples-google-workspace

Although it is not a web site, it is an example of a client that operates Google Workspace.


## Table of Contents <!-- omit in toc -->

- [examples-google-workspace](#examples-google-workspace)
  - [Examples](#examples)
    - [Getting started](#getting-started)
    - [Google Workspace apps for Python](#google-workspace-apps-for-python)
  - [Learn more](#learn-more)
  - [Configure Google Cloud API](#configure-google-cloud-api)
    - [Enable APIs](#enable-apis)
    - [When use service account (silent login)](#when-use-service-account-silent-login)
    - [When use user account (OAuth login)](#when-use-user-account-oauth-login)
  - [User credentials provided by using the gcloud CLI(OPTIONAL)](#user-credentials-provided-by-using-the-gcloud-clioptional)
  - [Development](#development)
    - [How the project was initialized](#how-the-project-was-initialized)

## Examples

### Getting started

Show help command:

```shell
examples-google-cli -h
```

### Google Workspace apps for Python

- [`auth` - Google Auth](./src/examples_google_workspace/auth/README.md)
- [`drive` - Google Drive API example](./src/examples_google_workspace//drive/README.md)
- [`docs` - Google Docs API example](./src/examples_google_workspace/docs/README.md)
- [`sheets` - Google Sheets API example](./src/examples_google_workspace/sheets/README.md)
- [`calendar` - Google Calendar API example](./src/examples_google_workspace/calendar/README.md)
- [`chat` - Google Chat API example](./src/examples_google_workspace/chat/README.md)
- [`gmail` - Google Gmail API example](./src/examples_google_workspace/gmail/README.md)


## Learn more

- [Enhance Google Workspace apps](https://developers.google.com/workspace?hl=ja)


## Configure Google Cloud API

Goto google cloud console:

- <https://console.cloud.google.com/welcome>

### Enable APIs

1. APIs & Services > Library
2. Enable [Google Drive API] and [Google Sheets API]

### When use service account (silent login)

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

### When use user account (OAuth login)

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


## User credentials provided by using the gcloud CLI(OPTIONAL)

Download gcloud CLI:

- <https://cloud.google.com/sdk/docs/install?hl=ja>

Initialize the CLI:

```shell
gcloud init
```

Select the project you created in the Google Cloud Console.

Provides authentication information to the Application Default Credentials (ADC):

```shell
gcloud auth application-default login --scopes=https://www.googleapis.com/auth/drive.readonly --client-id-file=/workspaces/examples-py-web/src/examples-google-workspace/credentials.json
```


## Development

### How the project was initialized

This project was initialized with the following command:

```shell
rye init --script
rye add --dev pytest-cov

rye add pyyaml
rye add --dev types-PyYAML

rye add google-api-python-client google-auth-httplib2 google-auth-oauthlib
rye add google-apps-chat
rye add gspread

rye sync
```
