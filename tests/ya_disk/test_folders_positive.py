import allure
import pytest

from utils.parsers import parse_response


@allure.epic("Yandex Disk API")
@allure.feature("Folders")
class TestFoldersPositive:

    @pytest.mark.ya_disk
    @allure.story("Создание папки")
    @allure.title("TC-FOL-01: PUT /v1/disk/resources — создание папки с валидным именем")
    def test_create_folder(self, ya_api, folder_for_create):
        status_code, body = parse_response(ya_api.create_folder(folder_for_create))
        assert status_code == 201, "Ожидался статус 201 Created"
        assert "href" in body, "В ответе отсутствует поле href"
        assert "method" in body, "В ответе отсутствует поле method"


    @pytest.mark.ya_disk
    @allure.story("Удаление папки")
    @allure.title("TC-FOL-03: DELETE /v1/disk/resources — удаление папки в корзину")
    def test_delete_folder(self, ya_api, folder_for_delete):
        response = ya_api.delete_resource(folder_for_delete)
        assert response.status_code == 204, "Ожидался статус 204 No Content"


    @pytest.mark.ya_disk
    @allure.story("Восстановление папки")
    @allure.title("TC-FOL-05: PUT /v1/disk/trash/resources/restore — восстановление папки из корзины")
    def test_restore_folder(self, ya_api, folder_for_restore):
        status_code, body = parse_response(ya_api.restore_from_trash(folder_for_restore))
        assert status_code == 201, "Ожидался статус 201 Created"
        assert "href" in body, "В ответе отсутствует поле href"
        assert "method" in body, "В ответе отсутствует поле method"
