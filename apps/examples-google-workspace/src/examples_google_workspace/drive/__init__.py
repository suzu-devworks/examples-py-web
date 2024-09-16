from argparse import ArgumentParser, Namespace

from . import quickstart


def _exec_list(args: Namespace) -> None:
    from examples_google_workspace.auth import get_credentials
    from examples_google_workspace.drive.list import list_items

    creds = get_credentials(args.auth_type, args.credential_file)
    list_items(creds, args.parent_id)
    pass


def configure_arguments(parser: ArgumentParser) -> None:
    sub = parser.add_subparsers()

    quick_parser = sub.add_parser("quickstart", help="Drive V3 Python Quickstart.")
    quick_parser.set_defaults(exec=lambda *args, **kwargs: quickstart.main())

    list_parser = sub.add_parser("list", help="list a drive")
    list_parser.add_argument(
        "-d",
        "--dir",
        dest="parent_id",
        help="parent directory id",
        default=None,
    )
    list_parser.set_defaults(exec=lambda args: _exec_list(args))
