from argparse import ArgumentParser

from . import quickstart


def configure_arguments(parser: ArgumentParser) -> None:
    sub = parser.add_subparsers()

    quick_parser = sub.add_parser("quickstart", help="Gmail Python Quickstart.")
    quick_parser.set_defaults(exec=lambda *args, **kwargs: quickstart.main())
