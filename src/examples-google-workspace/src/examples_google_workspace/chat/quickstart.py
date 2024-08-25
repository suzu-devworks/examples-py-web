# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START chat_quickstart]
# from __future__ import print_function

import os.path

from google.apps import chat_v1 as google_chat
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/chat.spaces.readonly"]


def main() -> None:
    """Shows basic usage of the Google Chat API."""
    # Because tokens with different scopes are cached.
    token_cache = "token.chat.json"
    # spell-checker:words creds
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(token_cache):
        creds = Credentials.from_authorized_user_file(token_cache, SCOPES)  # type: ignore[no-untyped-call]
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())  # type: ignore[no-untyped-call]
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token_cache, "w") as token:
            token.write(creds.to_json())

    try:
        # Create a client
        client = google_chat.ChatServiceClient(credentials=creds, client_options={"scopes": SCOPES})

        # Initialize request argument(s)
        request = google_chat.ListSpacesRequest(
            # Filter spaces by space type (SPACE or GROUP_CHAT or DIRECT_MESSAGE)
            filter='space_type = "SPACE"'
        )

        # Make the request
        page_result = client.list_spaces(request)

        # Handle the response. Iterating over page_result will yield results and
        # resolve additional pages automatically.
        for response in page_result:
            print(response)
    except Exception as error:
        # TODO(developer) - Handle errors from Chat API.
        print(f"An error occurred: {error}")


# if __name__ == "__main__":
#     main()
# [END chat_quickstart]
