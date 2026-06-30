import requests

from config.base_config import Config
from api_clients.api_helper import ApiHelper
from data.test_data import (
    YA_DISK_ENDPOINT,
    YA_DISK_RESOURCES_ENDPOINT,
    YA_DISK_TRASH_ENDPOINT,
    YA_DISK_TRASH_RESTORE_ENDPOINT)


class YandexDiskApi(ApiHelper):

    def __init__(self, token: str = Config.YA_DISK_TOKEN):
        super().__init__(
            base_url=Config.YA_DISK_BASE_URL,
            token=token,
        )

    def get_disk_info(self) -> requests.Response:
        return self.get(YA_DISK_ENDPOINT)

    def create_folder(self, path: str) -> requests.Response:
        return self.put(YA_DISK_RESOURCES_ENDPOINT, params={"path": path})

    def delete_resource(self, path: str, permanently: bool = False) -> requests.Response:
        return self.delete(YA_DISK_RESOURCES_ENDPOINT, params={"path": path, "permanently": str(permanently).lower()})

    def get_trash_resources(self) -> requests.Response:
        return self.get(YA_DISK_TRASH_ENDPOINT, params={"path": "/"})

    def restore_from_trash(self, path: str) -> requests.Response:
        return self.put(YA_DISK_TRASH_RESTORE_ENDPOINT, params={"path": path})

    def clear_trash(self) -> requests.Response:
        return self.delete(YA_DISK_TRASH_ENDPOINT)

    @staticmethod
    def parse_response(response: requests.Response) -> tuple[int, dict]:
        return response.status_code, response.json()
