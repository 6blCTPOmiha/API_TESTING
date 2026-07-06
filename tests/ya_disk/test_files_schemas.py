import allure
import pytest
import json
import jsonschema

from utils.parsers import parse_response


@allure.epic("Yandex Disk API")
@allure.feature("Files")
class TestFilesSchema:

    @pytest.mark.ya_disk_files
    @allure.title("TC-7: GET /v1/disk/resources/files — валидация JSON Schema")
    def test_get_files_list_schema(self, ya_api):
        status_code, body = parse_response(ya_api.get_files())
        assert status_code == 200, "Ожидался статус 200 OK"
        with open("data/schemas.json", encoding="utf-8") as f:
            schema = json.load(f)
        jsonschema.validate(instance=body, schema=schema)
