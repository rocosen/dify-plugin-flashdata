from typing import Any

from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError

from flashdata.client import FlashDataClient, FlashDataError
from flashdata.parameters import storage_config


class FlashDataProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        try:
            if credentials.get("download_storage"):
                storage_config(credentials["download_storage"])
            FlashDataClient(credentials.get("api_key")).validate_credentials()
        except FlashDataError as error:
            raise ToolProviderCredentialValidationError(str(error)) from None
