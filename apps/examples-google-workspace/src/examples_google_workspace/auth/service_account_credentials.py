from logging import getLogger

from google.oauth2 import service_account

_logger = getLogger(__name__)


def get_credentials(file_name: str, scopes: list[str]) -> service_account.Credentials:
    credentials = service_account.Credentials.from_service_account_file(file_name)  # type: ignore[no-untyped-call]
    scoped_credentials: service_account.Credentials = credentials.with_scopes(scopes)

    _logger.debug(scoped_credentials)
    return scoped_credentials
