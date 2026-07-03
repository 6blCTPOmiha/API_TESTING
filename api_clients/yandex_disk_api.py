import requests

from config.base_config import Config
from api_clients.api_helper import ApiHelper
from data.test_data import (
    YA_DISK_UPLOAD_ENDPOINT,
    YA_DISK_COPY_ENDPOINT,
    YA_DISK_DOWNLOAD_ENDPOINT,
    YA_DISK_FILES_ENDPOINT,
    YA_DISK_ENDPOINT,
    YA_DISK_RESOURCES_ENDPOINT,
    YA_DISK_TRASH_ENDPOINT,
    YA_DISK_TRASH_RESTORE_ENDPOINT)
from data.models import (
    UploadLinkRequest,
    CopyResourceRequest,
    DownloadLinkRequest,
    CreateFolderRequest,
    DeleteResourceRequest)


class YandexDiskApi(ApiHelper):

    def __init__(self, token: str = Config.YA_DISK_TOKEN):
        super().__init__(
            base_url=Config.YA_DISK_BASE_URL,
            token=token,
        )

    def get_disk_info(self) -> requests.Response:
        return self.get(YA_DISK_ENDPOINT)

    def create_folder(self, request: CreateFolderRequest) -> requests.Response:
        return self.put(YA_DISK_RESOURCES_ENDPOINT, params=request.to_params())

    def delete_resource(self, request: DeleteResourceRequest) -> requests.Response:
        return self.delete(YA_DISK_RESOURCES_ENDPOINT, params=request.to_params())

    def get_trash_resources(self) -> requests.Response:
        return self.get(YA_DISK_TRASH_ENDPOINT, params={"path": "/"})

    def restore_from_trash(self, path: str) -> requests.Response:
        return self.put(YA_DISK_TRASH_RESTORE_ENDPOINT, params={"path": path})

    def clear_trash(self) -> requests.Response:
        return self.delete(YA_DISK_TRASH_ENDPOINT)

    def get_upload_link_response(self, request: UploadLinkRequest) -> requests.Response:
        return self.get(YA_DISK_UPLOAD_ENDPOINT, params=request.to_params())

    def upload_file(self, upload_url: str, file_path: str) -> requests.Response:
        with open(file_path, "rb") as f:
            return self.put_by_url(upload_url, data=f)

    def copy_resource(self, request: CopyResourceRequest, from_path: str) -> requests.Response:
        return self.post(
            YA_DISK_COPY_ENDPOINT,
            params=request.to_params(from_path)
        )

    def get_download_link(self, request: DownloadLinkRequest) -> requests.Response:
        return self.get(YA_DISK_DOWNLOAD_ENDPOINT, params=request.to_params())

    def download_file(self, download_url: str) -> requests.Response:
        return self.get_by_url(download_url)

    def get_files(self) -> requests.Response:
        return self.get(YA_DISK_FILES_ENDPOINT)
