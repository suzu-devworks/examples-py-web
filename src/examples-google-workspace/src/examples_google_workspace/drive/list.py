from logging import getLogger

from googleapiclient.discovery import Resource, build
from googleapiclient.errors import HttpError

from examples_google_workspace.auth import Credentials

logger = getLogger(__name__)


def list_items(
    creds: Credentials,
    parent_id: str | None,
) -> None:
    try:
        # spell-checker:words creds
        service: Resource = build("drive", "v3", credentials=creds, cache_discovery=False)

        # fmt: off
        query = (
            "mimeType!='application/vnd.google-apps.folder'" +
            " and trashed=false")
        # fmt: on

        if parent_id:
            query += f" and '{parent_id}' in parents"

        # Call the Drive v3 API
        results = (
            service.files()
            .list(
                q=query,
                pageSize=10,
                fields="nextPageToken, files(id, name)",
            )
            .execute()
        )
        items = results.get("files", [])

        if not items:
            logger.warn("No files found.")
            return

        logger.info("Files:")
        for item in items:
            logger.info("  {0} ({1})".format(item["name"], item["id"]))

    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        logger.exception(f"An error occurred: {error}")
