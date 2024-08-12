from argparse import ArgumentParser
from logging import getLogger

import google.auth
from google.oauth2 import credentials, service_account

from . import service_account_credentials, user_account_credentials
from .account_types import AccountTypes

# use credentials to create a client to interact with the Google Drive API.
# see also: https://developers.google.com/identity/protocols/oauth2/scopes?hl=ja
SCOPES = [
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/gmail.compose",
]

_logger = getLogger(__name__)


def get_credentials(
    auth_type: AccountTypes,
    file_name: str,
) -> credentials.Credentials | service_account.Credentials:
    _logger.info("auth_type: %s", auth_type)
    _logger.info("file_name: %s", file_name)

    # spell-checker:words creds
    creds: credentials.Credentials | service_account.Credentials
    match auth_type:
        case AccountTypes.user:
            creds = user_account_credentials.get_credentials(file_name, SCOPES)

        case AccountTypes.service:
            creds = service_account_credentials.get_credentials(file_name, SCOPES)

        case _:
            creds, _ = google.auth.default(scopes=SCOPES)  # type: ignore[no-untyped-call]

    return creds


def configure_arguments(parser: ArgumentParser) -> None:

    parser.add_argument(
        "-A",
        "--auth",
        type=lambda s: AccountTypes.from_string(s),
        choices=list(AccountTypes),
        dest="auth_type",
        help="select auth account type",
        default=AccountTypes.default,
    )

    parser.add_argument(
        "-c",
        "--credential-file",
        help="specify the credential file (default: %(default)s)",
        default="credentials.json",
    )
