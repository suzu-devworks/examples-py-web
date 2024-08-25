from argparse import ArgumentParser, Namespace
from datetime import datetime
from logging import getLogger

import gspread

#  spell-checker:words gspread
from examples_google_workspace.auth.account_types import AccountTypes

_logger = getLogger(__name__)


def _create_client(
    auth_type: AccountTypes,
    file_name: str,
) -> gspread.client.Client:
    _logger.info("auth_type: %s", auth_type)
    _logger.info("file_name: %s", file_name)

    # spell-checker:words creds
    client: gspread.client.Client
    match auth_type:
        case AccountTypes.user:
            client = gspread.auth.oauth(credentials_filename=file_name)

        case AccountTypes.service:
            client = gspread.auth.service_account(filename=file_name)

        case _:
            raise ValueError("not supported.")

    return client


def _create_file(args: Namespace) -> str:
    title: str = args.title.strip()
    parent_id: str = args.parent_id.strip() if args.parent_id else None

    client = _create_client(args.auth_type, args.credential_file)

    if parent_id:
        _logger.info(f"Parent ID: {parent_id}")

    _logger.debug("call create.")
    spreadsheet = client.create(title=title, folder_id=parent_id)

    # If you're using a service account, you'll need to share the spreadsheet via email.
    # spreadsheet.share("otto@example.com", perm_type="user", role="writer", notify=False)

    _logger.info(f"Spreadsheet ID: {spreadsheet.id} ({spreadsheet.title})")
    _logger.info(f"Spreadsheet URL: {spreadsheet.url}")
    _logger.info(f"  creationTime >>> {spreadsheet.creationTime}")
    _logger.info(f"  lastUpdateTime >>> {spreadsheet.lastUpdateTime}")

    return str(spreadsheet.id)


def _add_sheet(args: Namespace) -> None:
    sheet_name: str = args.sheet_name.strip()
    spreadsheet_id: str = args.fileId

    client = _create_client(args.auth_type, args.credential_file)

    spreadsheet = client.open_by_key(spreadsheet_id)

    _logger.debug("call add_worksheet.")
    worksheet = spreadsheet.add_worksheet(title=sheet_name, rows=20, cols=12)
    worksheet.update_tab_color("cc0066")

    _logger.info(f"Updated Spreadsheet ID: {spreadsheet.id} ")
    _logger.info(f"Sheet ID: {worksheet.id} ({worksheet.title})")

    return


def _write_data(args: Namespace) -> None:
    spreadsheet_id: str = args.fileId

    client = _create_client(args.auth_type, args.credential_file)

    spreadsheet = client.open_by_key(spreadsheet_id)
    worksheet = spreadsheet.get_worksheet(0)

    # clear range data
    _logger.debug("call batch_clear.")
    # all clear : worksheet.clear()
    response = worksheet.batch_clear(["A1:H50"])

    _logger.info(f"Spreadsheet ID: {response.get('spreadsheetId')}")
    _logger.info(f" clearedRanges: {response.get('clearedRanges')}")

    # write range data
    # fmt: off
    values = ([
        ["A", "B"],
        ["C", str(datetime.now())],
    ])
    # fmt: on

    _logger.debug("call batch_clear.")
    response = worksheet.update(values, "A1:C2")

    _logger.info(f"Spreadsheet ID: {response.get('spreadsheetId')}")
    _logger.info(f" updatedRange: {response.get('updatedRange')}")
    _logger.info(f" updatedCells: {response.get('updatedCells')}")

    # write multiple range data
    # fmt: off
    values = ([
        ["F", "B"],
        ["C", str(datetime.now())],
    ])

    _logger.debug("call batch_update.")
    response = worksheet.batch_update([{
        'range': 'D4',
        'values': values,
    }, {
        'range': 'D8',
        'values': values,
    }])

    _logger.info(f"Spreadsheet ID: {response.get('spreadsheetId')}")
    _logger.info(f" totalUpdatedCells: {response.get('totalUpdatedCells')}")

    # format
    formats: list[gspread.worksheet.CellFormat] = [
        {
            "range": "A1:C1",
            "format": {
                "textFormat": {
                    "bold": True,
                },
                "backgroundColorStyle": {
                    "rgbColor": {"red": 1.0, "green": 0.3, "blue": 0.3},
                }
            },
        },
        {
            "range": "A2:C2",
            "format": {
                "textFormat": {
                    "fontSize": 16,
                    "foregroundColor": {"red": (10 / 255.0) , "green": (50 / 255.0), "blue": float(100 / 255.0)},
                },
            },
        },
    ]
    _logger.debug("call batch_format.")
    response = worksheet.batch_format(formats)

    _logger.info(f"Spreadsheet ID: {response.get('spreadsheetId')}")
    _logger.info(f"len(replies): {len(response.get('replies', []))}")

    return


def _read_data(args: Namespace) -> None:
    spreadsheet_id: str = args.fileId

    client = _create_client(args.auth_type, args.credential_file)

    spreadsheet = client.open_by_key(spreadsheet_id)
    worksheet = spreadsheet.sheet1

    _logger.debug("call any ...")
    cell = worksheet.acell("B2")
    _logger.info(f"'{cell.address}' >>> {cell.value}")
    cell = worksheet.cell(2, 1)
    _logger.info(f"'{cell.address}' >>> {cell.value}")
    cell = worksheet.acell("A1:C2")
    _logger.info(f"'{cell.address}' >>> {cell.value}")

    values = worksheet.row_values(1)
    _logger.info(f" >>> {values}")
    values = worksheet.col_values(5)
    _logger.info(f" >>> {values}")

    list_of_lists = worksheet.get_all_values()
    _logger.info(f" >>> {list_of_lists}")

    _logger.debug("call get.")
    values = worksheet.get("A1:B2")

    _logger.info(f"A1:B2 >>> {values}")

    _logger.debug("call batch_get.")
    values_list = worksheet.batch_get(["D4:F5", "D8:F9"])

    for values in values_list:
        _logger.info(f"{values.range} >>> {values}")

    return


def _delete_file(args: Namespace) -> None:
    spreadsheet_id: str = args.fileId
    force: bool = args.force

    client = _create_client(args.auth_type, args.credential_file)

    if force:
        _logger.debug("call del_spreadsheet.")
        client.del_spreadsheet(spreadsheet_id)

        _logger.info(f"deleted(force): {spreadsheet_id} ")
    else:
        # TODO move to trashed ?
        pass

    return


def configure_parser(parser: ArgumentParser) -> None:
    subparsers = parser.add_subparsers(
        title="Python API for Google Sheets example",
        help="choose command",
        required=True,
    )

    # create
    create_parser = subparsers.add_parser("create", help="create new spreadsheet")
    create_parser.add_argument(
        "-t",
        "--title",
        dest="title",
        help="file title",
        default="A new spreadsheet",
    )
    create_parser.add_argument(
        "-d",
        "--dir",
        dest="parent_id",
        help="parent directory id",
        default=None,
    )
    create_parser.set_defaults(exec=lambda args: _create_file(args))

    # add sheet
    sheet_parser = subparsers.add_parser("add", help="add sheet in spreadsheet sample")
    sheet_parser.add_argument(
        "fileId",
        help="fileId",
        type=str,
    )
    sheet_parser.add_argument(
        "-n",
        "--name",
        dest="sheet_name",
        help="sheet name",
        default="new sheet",
    )
    sheet_parser.set_defaults(exec=lambda args: _add_sheet(args))

    # write
    write_parser = subparsers.add_parser("write", help="write data sample")
    write_parser.add_argument(
        "fileId",
        help="fileId",
        type=str,
    )
    write_parser.set_defaults(exec=lambda args: _write_data(args))

    # read
    read_parser = subparsers.add_parser("read", help="read data sample")
    read_parser.add_argument(
        "fileId",
        help="fileId",
        type=str,
    )
    read_parser.set_defaults(exec=lambda args: _read_data(args))

    # delete
    delete_parser = subparsers.add_parser("delete", help="delete spreadsheet sample")
    delete_parser.add_argument(
        "fileId",
        help="fileId",
        type=str,
    )
    delete_parser.add_argument(
        "-f",
        "--force",
        action="store_true",
        dest="force",
        help="force delete spread sheet.",
        default=False,
    )
    delete_parser.set_defaults(exec=lambda args: _delete_file(args))
