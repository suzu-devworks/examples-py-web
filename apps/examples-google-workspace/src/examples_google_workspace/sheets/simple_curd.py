from argparse import ArgumentParser, Namespace
from datetime import datetime
from logging import getLogger
from typing import Any

from googleapiclient.discovery import Resource, build
from googleapiclient.errors import HttpError

from examples_google_workspace.auth import Credentials, get_credentials

logger = getLogger(__name__)


def _build_drive_resource(credentials: Credentials) -> Resource:
    return build("drive", "v3", credentials=credentials, cache_discovery=False)


def _build_sheets_resource(credentials: Credentials) -> Resource:
    return build("sheets", "v4", credentials=credentials, cache_discovery=False)


def _create_file(args: Namespace) -> str:
    title: str = args.title.strip()
    parent_id: str = args.parent_id.strip() if args.parent_id else None

    creds = get_credentials(args.auth_type, args.credential_file)

    try:
        # create file
        drive_service = _build_drive_resource(credentials=creds)

        file_metadata: dict[str, Any] = {
            "name": title,
            "mimeType": "application/vnd.google-apps.spreadsheet",
        }
        if parent_id:
            file_metadata["parents"] = [parent_id]
            logger.info(f"Parent ID: {parent_id}")

        logger.debug("Request create.")
        response = drive_service.files().create(body=file_metadata, fields="id").execute()

        file_id = response.get("id")
        logger.debug(f"File ID: {file_id}")

        # get sheet
        sheet_service = _build_sheets_resource(credentials=creds)

        logger.debug("Request get.")
        response = sheet_service.spreadsheets().get(spreadsheetId=file_id).execute()

        spreadsheet_id: str = response.get("spreadsheetId")
        spreadsheet_url = response.get("spreadsheetUrl")
        spreadsheet_title = response.get("properties").get("title")
        logger.info(f"Spreadsheet ID: {spreadsheet_id} ({spreadsheet_title})")
        logger.info(f"Spreadsheet URL: {spreadsheet_url}")

        return spreadsheet_id

    except HttpError:
        logger.exception("An error occurred.")
        raise


def _add_sheet(args: Namespace) -> None:
    spreadsheet_id: str = args.fileId

    creds = get_credentials(args.auth_type, args.credential_file)
    sheet_service = _build_sheets_resource(credentials=creds)

    try:
        # add sheet
        properties = {
            "gridProperties": {"rowCount": 20, "columnCount": 12},
            "tabColor": {"red": 1.0, "green": 0.3, "blue": 0.4},
        }

        requests = []
        requests.append({"addSheet": {"properties": properties}})
        request_body = {
            # A list of updates to apply to the spreadsheet.
            # Requests will be applied in the order they are specified.
            # If any request is not valid, no requests will be applied.
            "requests": requests
        }

        logger.debug("Request batchUpdate.")
        response = sheet_service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id, body=request_body).execute()

        spreadsheet_id = response.get("spreadsheetId")
        sheet = response.get("replies")[0].get("addSheet").get("properties")
        sheet_id = sheet.get("sheetId")
        sheet_title = sheet.get("title")
        logger.info(f"Updated Spreadsheet ID: {spreadsheet_id} ")
        logger.info(f"Sheet ID: {sheet_id} ({sheet_title})")

    except HttpError:
        logger.exception("An error occurred.")
        raise


def _write_data(args: Namespace) -> None:
    spreadsheet_id: str = args.fileId

    creds = get_credentials(args.auth_type, args.credential_file)
    sheet_service = _build_sheets_resource(credentials=creds)

    try:
        request_body: dict[str, Any]

        # clear values

        range = "'シート1'!A1:H50"

        logger.debug("Request value clear.")
        response = sheet_service.spreadsheets().values().clear(spreadsheetId=spreadsheet_id, range=range).execute()

        logger.info(f"Spreadsheet ID: {response.get('spreadsheetId')}")
        logger.info(f" clearedRange: {response.get('clearedRange')}")

        # write range data

        # fmt: off
        values = ([
            ["A", "B"],
            ["C", str(datetime.now())],
        ])
        # fmt: on
        request_body = {"values": values}
        request_range = "'シート1'!A1:C2"

        logger.debug("Request value update.")
        response = (
            sheet_service.spreadsheets()
            .values()
            .update(
                spreadsheetId=spreadsheet_id,
                range=request_range,
                valueInputOption="USER_ENTERED",
                body=request_body,
            )
            .execute()
        )
        logger.info(f"Spreadsheet ID: {response.get('spreadsheetId')}")
        logger.info(f" updatedRange: {response.get('updatedRange')}")
        logger.info(f" updatedCells: {response.get('updatedCells')}")

        # write multiple range data

        # fmt: off
        values = ([
            ["F", "B"],
            ["C", str(datetime.now())],
        ])
        # fmt: on
        data = [
            {"range": "'シート1'!D4", "values": values},
            {"range": "'シート1'!D8", "values": values},
        ]
        request_body = {"valueInputOption": "USER_ENTERED", "data": data}

        logger.debug("Request value batchUpdate.")
        response = (
            sheet_service.spreadsheets()
            .values()
            .batchUpdate(spreadsheetId=spreadsheet_id, body=request_body)
            .execute()
        )

        logger.info(f"Spreadsheet ID: {response.get('spreadsheetId')}")
        logger.info(f" totalUpdatedCells: {response.get('totalUpdatedCells')}")

        # append table data

        # fmt: off
        values = ([
            ["G", "B"],
            ["C", str(datetime.now())],
        ])
        # fmt: on
        request_body = {"values": values}

        logger.debug("Request append.")
        response = (
            sheet_service.spreadsheets()
            .values()
            .append(
                spreadsheetId=spreadsheet_id,
                range="A1",
                valueInputOption="USER_ENTERED",
                body=request_body,
            )
            .execute()
        )
        logger.info(f"Spreadsheet ID: {response.get('spreadsheetId')}")
        logger.info(f" tableRange: {response.get('tableRange')}")
        logger.info(f" updatedCells: {response.get('updates').get('updatedCells')}")

    except HttpError:
        logger.exception("An error occurred.")


def _read_data(args: Namespace) -> None:
    spreadsheet_id: str = args.fileId

    creds = get_credentials(args.auth_type, args.credential_file)
    sheet_service = _build_sheets_resource(credentials=creds)

    try:
        # read range data
        range_name = "'シート1'!A1:C4"

        logger.debug("Request value get.")
        response = sheet_service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()

        values = response.get("values", [])
        logger.info(f"{response.get('range')} >>> {values}")

        # read multiple range data
        range_names = [
            "D4:F5",
            "D8:F9",
        ]

        logger.debug("Request value batchGet.")
        response = (
            sheet_service.spreadsheets().values().batchGet(spreadsheetId=spreadsheet_id, ranges=range_names).execute()
        )

        logger.info(f"Spreadsheet ID: {response.get('spreadsheetId')}")
        response = response.get("valueRanges", [])
        for reply in response:
            values = reply.get("values", [])
            logger.info(f"{reply.get('range')} >>> {values}")

    except HttpError:
        logger.exception("An error occurred.")


def _delete_file(args: Namespace) -> None:
    file_id: str = args.fileId
    force: bool = args.force

    creds = get_credentials(args.auth_type, args.credential_file)

    try:
        # delete file(drive)
        drive_service = _build_drive_resource(credentials=creds)

        if force:
            logger.debug("Request files delete.")
            response = drive_service.files().delete(fileId=file_id).execute()

            logger.info(f"deleted(force) : {file_id}")

        else:
            logger.debug("Request files move to trashed.")
            response = drive_service.files().update(fileId=file_id, body={"trashed": True}).execute()  # noqa F841

            logger.info(f"deleted : {file_id}")

    except HttpError:
        logger.exception("An error occurred.")


def configure_parser(parser: ArgumentParser) -> None:
    subparsers = parser.add_subparsers(
        title="Google Sheets API example",
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
        default="無題のスプレッドシート",
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
