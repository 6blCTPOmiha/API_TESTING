import pytest

from helpers.db_helper import DbHelper
from helpers.wordpress_api import WordPressApi
from helpers.yandex_disk_api import YandexDiskApi
from data.test_data import FolderData


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
def ya_api_no_token() -> YandexDiskApi:
    client = YandexDiskApi(token="")
    yield client
    client.close()


@pytest.fixture
def folder_for_delete(ya_api) -> str:
    ya_api.create_folder(FolderData.TEST_FOLDER_PATH)
    yield FolderData.TEST_FOLDER_PATH
    ya_api.clear_trash()


@pytest.fixture
def folder_for_restore(ya_api) -> str:
    ya_api.create_folder(FolderData.TEST_FOLDER_PATH)
    ya_api.delete_resource(FolderData.TEST_FOLDER_PATH)
    trash_name = ya_api.find_in_trash(FolderData.TEST_FOLDER_PATH)
    yield trash_name
    ya_api.delete_resource(FolderData.TEST_FOLDER_PATH, permanently=True)


@pytest.fixture
def folder_for_create(ya_api):
    yield FolderData.TEST_FOLDER_PATH
    ya_api.delete_resource(FolderData.TEST_FOLDER_PATH, permanently=True)


@pytest.fixture
def existing_folder(ya_api):
    ya_api.create_folder(FolderData.TEST_FOLDER_PATH)
    yield FolderData.TEST_FOLDER_PATH
    ya_api.delete_resource(FolderData.TEST_FOLDER_PATH, permanently=True)
