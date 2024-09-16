from argparse import ArgumentParser

from . import gspread_crud, quickstart, simple_curd


def configure_arguments(parser: ArgumentParser) -> None:
    sub = parser.add_subparsers()

    quick_parser = sub.add_parser("quickstart", help="Google Sheets Python Quickstart.")
    quick_parser.set_defaults(exec=lambda *args, **kwargs: quickstart.main())

    simple = sub.add_parser("simple", help="Simple CURD example with Google Sheets API.")
    simple_curd.configure_parser(simple)

    gspread = sub.add_parser("gspread", help="CRUD example using the gspread library.")
    gspread_crud.configure_parser(gspread)
