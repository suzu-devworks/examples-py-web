from argparse import ArgumentParser, Namespace, RawTextHelpFormatter
from logging import getLogger
from logging.config import dictConfig

from examples_google_workspace.resources import get_logging_resource

from .arguments import configure_arguments

dictConfig(get_logging_resource("logging_config.yaml"))
_logger = getLogger(__name__)


def _parse_arguments() -> Namespace:
    parser = ArgumentParser(
        description="Google Cloud API programming examples.",
        formatter_class=RawTextHelpFormatter,
    )
    configure_arguments(parser)

    # auth
    from examples_google_workspace.auth import configure_arguments as configure_auth

    configure_auth(parser)

    subparsers = parser.add_subparsers()

    # drive
    from examples_google_workspace.drive import configure_arguments as configure_drive

    drive_parser = subparsers.add_parser("drive", help="Google Drive API example")
    configure_drive(drive_parser)

    # docs
    from examples_google_workspace.docs import configure_arguments as configure_docs

    docs_parser = subparsers.add_parser("docs", help="Google Docs API example")
    configure_docs(docs_parser)

    # sheets
    from examples_google_workspace.sheets import configure_arguments as configure_sheets

    sheets_parser = subparsers.add_parser("sheets", help="Google Sheets API example")
    configure_sheets(sheets_parser)

    # calendar
    from examples_google_workspace.calendar import (
        configure_arguments as configure_calendar,
    )

    calendar_parser = subparsers.add_parser("calendar", help="Google Calendar API example")
    configure_calendar(calendar_parser)

    # chat
    from examples_google_workspace.chat import configure_arguments as configure_chat

    chat_parser = subparsers.add_parser("chat", help="Google Chat API example")
    configure_chat(chat_parser)

    # gmail
    from examples_google_workspace.gmail import configure_arguments as configure_gmail

    gmail_parser = subparsers.add_parser("gmail", help="Google Gmail API example")
    configure_gmail(gmail_parser)

    return parser.parse_args()


def main() -> int:
    args = _parse_arguments()

    try:
        args.exec(args)
        return 0

    except Exception:
        _logger.exception("Exiting due to an unhandled exception.")
        return 1
