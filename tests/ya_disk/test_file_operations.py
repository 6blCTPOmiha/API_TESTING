import allure
import pytest

from data.models import UploadResponse, ResourceResponse, ErrorResponse
from data.test_data import FileData
from utils.file_helper import FileHelper
from utils.parsers import parse_response


@allure.epic("Yandex Disk API")
@allure.feature("File Operations")
class TestFileOperations:

    @pytest.mark.ya_disk_files
    @allure.story("Загрузка и копирование файла")
    @allure.title("TC-3: Загрузка data.txt в input_data и копирование в output_data")
    def test_upload_and_copy_file(self, ya_api, upload_setup):

        local_file_path = upload_setup
        FileHelper.generate_data_txt(local_file_path)

        upload_link_status, upload_link_body = parse_response(
            ya_api.get_upload_link_response(FileData.INPUT_FILE_PATH)
        )
        assert upload_link_status == 200, "Ожидался статус 200 при получении ссылки на загрузку"

        upload_obj = UploadResponse.from_dict(upload_link_body)

        resp = ya_api.upload_file(upload_obj.href, local_file_path)
        assert resp.status_code == 201, "Ожидался статус 201 при загрузке файла"


        copy_status, copy_body = parse_response(
            ya_api.copy_resource(FileData.INPUT_FILE_PATH, FileData.OUTPUT_FILE_PATH)
        )
        assert copy_status == 201, "Ожидался статус 201 при копировании файла"
        
        copy_obj = ResourceResponse.from_dict(copy_body)
        assert copy_obj.href, "В ответе на копирование отсутствует поле href"
        assert copy_obj.method, "В ответе на копирование отсутствует поле method"


        conflict_status, conflict_body = parse_response(
            ya_api.copy_resource(FileData.INPUT_FILE_PATH, FileData.OUTPUT_FILE_PATH)
        )
        assert conflict_status == 409, "Ожидался статус 409 при повторном копировании"
        error = ErrorResponse.from_dict(conflict_body)
        assert error.error == FileData.ALREADY_EXISTS_ERROR
        assert error.description, "Поле description отсутствует в ответе 409"
        assert error.message, "Поле message отсутствует в ответе 409"

    @pytest.mark.ya_disk_files
    @allure.story("Скачивание файла")
    @allure.title("TC-4: Скачивание data.txt и сравнение с оригиналом")
    def test_download_and_compare_file(self, ya_api, download_setup):
        local_file_path = download_setup

        download_link_status, download_link_body = parse_response(
            ya_api.get_download_link(FileData.SDET_FILE_PATH)
        )
        assert download_link_status == 200, "Ожидался статус 200 при получении ссылки на скачивание"

        download_link = ResourceResponse.from_dict(download_link_body)
        assert download_link.href, "В ответе отсутствует поле href со ссылкой на скачивание"

        downloaded_content = FileHelper.normalize_text(ya_api.download_file(download_link.href).text)
        original_content = FileHelper.normalize_text(FileHelper.read_file(local_file_path))
        assert downloaded_content == original_content, "Содержимое скачанного файла не совпадает с оригиналом"
