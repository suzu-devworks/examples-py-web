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

    subparsers = parser.add_subparsers()

    # drive
    from examples_google_workspace.drive import configure_arguments as configure_drive

    drive_parser = subparsers.add_parser(
        "drive",
        help="drive api example",
        description="google drive api example",
    )
    configure_drive(drive_parser)

    return parser.parse_args()


def main() -> int:
    args = _parse_arguments()

    try:
        args.exec(args)
        return 0

    except Exception:
        _logger.exception("Exiting due to an unhandled exception.")
        return 1
