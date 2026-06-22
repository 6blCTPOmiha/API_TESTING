import allure
import pytest

from config.base_config import Config


@allure.epic("Yandex Disk API")
@allure.feature("Disk Info")
class TestDiskInfoPositive:

    @pytest.mark.ya_disk
    @allure.story("Получение информации о диске")
    @allure.title("TC-YA-01: GET /v1/disk с валидным токеном")
    def test_get_disk_info_status(self, ya_api):
        response = ya_api.get_disk_info()
        assert response.status_code == 200, "Ожидался статус 200 OK"

        body = ya_api.get_disk_info().json()
        login = body["user"]["login"]
        display_name = body["user"]["display_name"]
        assert login == Config.YA_DISK_LOGIN, "Поле login не соответствует данным пользователя"
        assert display_name == Config.YA_DISK_DISPLAY_NAME, "Поле display_name не соответствует данным пользователя"
