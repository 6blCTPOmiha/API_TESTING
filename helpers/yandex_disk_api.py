import requests

from config.base_config import Config
from helpers.api_helper import ApiHelper
from data.test_data import YA_DISK_ENDPOINT


class YandexDiskApi(ApiHelper):

    def __init__(self):
        super().__init__(
            base_url=Config.YA_DISK_BASE_URL,
            token=Config.YA_DISK_TOKEN,
        )

    def get_disk_info(self) -> requests.Response:
        return self.get(YA_DISK_ENDPOINT)
