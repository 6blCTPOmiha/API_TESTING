import pytest
import uuid

from api_clients.db_helper import DbHelper
from api_clients.wordpress_api import WordPressApi
from api_clients.yandex_disk_api import YandexDiskApi
from data.test_data import FolderData, FileData
from utils.file_helper import FileHelper
from utils.parsers import parse_response, find_resource_in_items


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


def make_unique_folder_name() -> str:
    return f"{FolderData.TEST_FOLDER_PREFIX}-{uuid.uuid4().hex[:8]}"


@pytest.fixture
def folder_for_create(ya_api):
    folder_name = make_unique_folder_name()
    yield folder_name
    ya_api.delete_resource(folder_name, permanently=True)


@pytest.fixture
def folder_for_delete(ya_api) -> str:
    folder_name = make_unique_folder_name()
    ya_api.create_folder(folder_name)
    yield folder_name
    ya_api.clear_trash()


@pytest.fixture
def folder_for_restore(ya_api) -> str:
    folder_name = make_unique_folder_name()
    ya_api.create_folder(folder_name)
    ya_api.delete_resource(folder_name)
    trash_body = parse_response(ya_api.get_trash_resources())[1]
    items = trash_body.get("_embedded", {}).get("items", [])
    trash_name = find_resource_in_items(items, folder_name)
    yield trash_name
    ya_api.delete_resource(folder_name, permanently=True)


@pytest.fixture
def existing_folder(ya_api):
    folder_name = make_unique_folder_name()
    ya_api.create_folder(folder_name)
    yield folder_name
    ya_api.delete_resource(folder_name, permanently=True)


@pytest.fixture
def upload_setup(ya_api, tmp_path):

    ya_api.create_folder(FileData.INPUT_FOLDER)
    ya_api.create_folder(FileData.OUTPUT_FOLDER)

    local_file_path = tmp_path / FileData.FILE_NAME
    yield str(local_file_path)

    ya_api.delete_resource(FileData.INPUT_FOLDER, permanently=True)
    ya_api.delete_resource(FileData.OUTPUT_FOLDER, permanently=True)


@pytest.fixture
def download_setup(ya_api, tmp_path):

    ya_api.create_folder(FileData.SDET_FOLDER)

    local_file_path = str(tmp_path / FileData.FILE_NAME)
    FileHelper.generate_data_txt(local_file_path)
    upload_link_status, upload_link_body = parse_response(
        ya_api.get_upload_link_response(FileData.SDET_FILE_PATH)
    )
    assert upload_link_status == 200, "Ожидался статус 200 при получении ссылки на загрузку"

    upload_url = upload_link_body["href"]
    resp = ya_api.upload_file(upload_url, local_file_path)
    assert resp.status_code == 201, "Ожидался статус 201 при загрузке файла"

    yield local_file_path

    ya_api.delete_resource(FileData.SDET_FOLDER, permanently=True)
