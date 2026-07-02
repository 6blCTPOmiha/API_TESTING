import allure
import pytest

from utils.parsers import parse_response


@allure.epic("Yandex Disk API")
@allure.feature("Disk Info")
class TestDiskInfoNegative:

    @pytest.mark.ya_disk
    @allure.story("Получение информации о диске")
    @allure.title("TC-YA-02: GET /v1/disk без токена")
    def test_get_disk_info_no_token(self, ya_api_no_token):
        status_code, body = parse_response(ya_api_no_token.get_disk_info())
        assert status_code == 401, "Ожидался статус 401 Unauthorized"
        assert body["error"] is not None, "Поле error отсутствует"
        assert body["description"] is not None, "Поле description отсутствует"
        assert body["message"] is not None, "Поле message отсутствует"
