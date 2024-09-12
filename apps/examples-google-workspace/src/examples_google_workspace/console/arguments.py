from argparse import ArgumentParser

from examples_google_workspace import __version__


def configure_arguments(parser: ArgumentParser) -> None:
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        help="show verbose output, -vv -vvv is even more.",
        default=0,
    )
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
        help="show version and exit",
    )
    parser.set_defaults(exec=lambda *args, **kwargs: parser.print_help())
