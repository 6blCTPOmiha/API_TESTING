import allure
import pytest

from data.test_data import FolderData
from utils.parsers import parse_response
from data.models import CreateFolderRequest, DeleteResourceRequest


@allure.epic("Yandex Disk API")
@allure.feature("Folders")
class TestFoldersNegative:

    @pytest.mark.ya_disk
    @allure.story("Создание папки")
    @allure.title("TC-FOL-02: PUT /v1/disk/resources — создание уже существующей папки")
    def test_create_folder_already_exists(self, ya_api, existing_folder):
        status_code, body = parse_response(ya_api.create_folder(CreateFolderRequest(path=existing_folder)))
        assert status_code == 409, "Ожидался статус 409 Conflict"
        assert body["error"] == FolderData.ALREADY_EXISTS_ERROR


    @pytest.mark.ya_disk
    @allure.story("Удаление папки")
    @allure.title("TC-FOL-04: DELETE /v1/disk/resources — удаление несуществующей папки")
    def test_delete_folder_not_existing(self, ya_api):
        status_code, body = parse_response(ya_api.delete_resource(DeleteResourceRequest(path=FolderData.NONEXISTENT_PATH)))
        assert status_code == 404, "Ожидался статус 404 Not Found"
        assert body["error"] == FolderData.NOT_FOUND_ERROR


    @pytest.mark.ya_disk
    @allure.story("Восстановление папки")
    @allure.title("TC-FOL-06: PUT /v1/disk/trash/resources/restore — восстановление несуществующей папки из корзины")
    def test_restore_folder_not_in_trash(self, ya_api):
        status_code, body = parse_response(ya_api.restore_from_trash(FolderData.NONEXISTENT_PATH))
        assert status_code == 404, "Ожидался статус 404 Not Found"
        assert body["error"] == FolderData.NOT_FOUND_ERROR
