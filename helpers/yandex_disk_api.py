import requests

from config.base_config import Config
from helpers.api_helper import ApiHelper
from data.test_data import YA_DISK_ENDPOINT


class YandexDiskApi(ApiHelper):

    def __init__(self, token: str = Config.YA_DISK_TOKEN):
        super().__init__(
            base_url=Config.YA_DISK_BASE_URL,
            token=token,
        )

    def get_disk_info(self) -> requests.Response:
        return self.get(YA_DISK_ENDPOINT)

    @staticmethod
    def parse_disk_info_response(response: requests.Response) -> tuple[int, dict]:
        return response.status_code, response.json()
