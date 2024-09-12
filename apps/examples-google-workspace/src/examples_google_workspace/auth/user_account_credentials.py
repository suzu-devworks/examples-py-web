import os
from logging import getLogger

from google.auth.transport.requests import Request
from google.oauth2 import credentials
from google_auth_oauthlib.flow import InstalledAppFlow

_logger = getLogger(__name__)


def get_credentials(file_name: str, scopes: list[str]) -> credentials.Credentials:
    # Because tokens with different scopes are cached.
    token_cache = "token.json"

    creds: credentials.Credentials | None = None

    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(token_cache):
        creds = credentials.Credentials.from_authorized_user_file(token_cache, scopes)  # type: ignore[no-untyped-call]

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())  # type: ignore[no-untyped-call]

        else:
            flow = InstalledAppFlow.from_client_secrets_file(file_name, scopes)
            creds = flow.run_local_server(port=0)

            if not creds:
                raise ValueError("illegal credential")

            # Save the credentials for the next run
            with open(token_cache, "w") as token:
                token.write(creds.to_json())  # type: ignore[no-untyped-call]

    _logger.debug(creds)
    return creds
