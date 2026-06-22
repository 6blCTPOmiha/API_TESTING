import pytest

from helpers.api_helper import ApiHelper
from helpers.db_helper import DbHelper
from helpers.wordpress_api import WordPressApi
from helpers.yandex_disk_api import YandexDiskApi
from config.base_config import Config



@pytest.fixture(scope="session")
def wp_api() -> WordPressApi:
    client = WordPressApi()
    yield client
    client.close()


@pytest.fixture(scope="session")
def db() -> DbHelper:
    helper = DbHelper()
    yield helper
    helper.close_connection()


@pytest.fixture(scope="session")
def ya_api() -> YandexDiskApi:
    client = YandexDiskApi()
    yield client
    client.close()


@pytest.fixture(scope="session")
def ya_api_no_token() -> ApiHelper:
    client = ApiHelper(base_url=Config.YA_DISK_BASE_URL)
    yield client
    client.close()
