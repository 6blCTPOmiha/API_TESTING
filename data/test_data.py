from config.base_config import Config

WP_POSTS_ENDPOINT = f"{Config.WP_REST_PREFIX}/wp/v2/posts"

YA_DISK_ENDPOINT = "/v1/disk"
YA_DISK_RESOURCES_ENDPOINT = "/v1/disk/resources"
YA_DISK_TRASH_ENDPOINT = "/v1/disk/trash/resources"
YA_DISK_TRASH_RESTORE_ENDPOINT = "/v1/disk/trash/resources/restore"


class PostData:
    VALID_TITLE = "Test Post"
    VALID_CONTENT = "Some content"
    VALID_STATUS = "publish"

    UPDATED_TITLE = "New post"
    UPDATED_CONTENT = "New content"

    VALID_PAYLOAD = {
        "title": VALID_TITLE,
        "content": VALID_CONTENT,
        "status": VALID_STATUS,
    }

    UPDATED_PAYLOAD = {"title": UPDATED_TITLE, "content": UPDATED_CONTENT, }

    STATUS_ONLY_PAYLOAD = {"status": VALID_STATUS}
    EMPTY_FIELDS_PAYLOAD = {"title": "", "content": ""}

    EMPTY_CONTENT_ERROR = "Содержимое, заголовок и отрывок пусты."
    INVALID_ID_ERROR = "Неверный ID записи."


class FolderData:
    TEST_FOLDER_PREFIX = "test-autotest-folder"
    ALREADY_EXISTS_ERROR = "DiskPathPointsToExistentDirectoryError"
    NONEXISTENT_PATH = "nonexistent-folder"
    NOT_FOUND_ERROR = "DiskNotFoundError"


YA_DISK_UPLOAD_ENDPOINT = "/v1/disk/resources/upload"
YA_DISK_COPY_ENDPOINT = "/v1/disk/resources/copy"
YA_DISK_DOWNLOAD_ENDPOINT = "/v1/disk/resources/download"
YA_DISK_FILES_ENDPOINT = "/v1/disk/resources/files"


class FileData:
    FILE_NAME = "data.txt"
    DATA_TXT_CONTENT = "username=SDET\npassword=secret_key"

    INPUT_FOLDER = "input_data"
    OUTPUT_FOLDER = "output_data"
    SDET_FOLDER = "sdet_data"

    INPUT_FILE_PATH = f"{INPUT_FOLDER}/{FILE_NAME}"
    OUTPUT_FILE_PATH = f"{OUTPUT_FOLDER}/{FILE_NAME}"
    SDET_FILE_PATH = f"{SDET_FOLDER}/{FILE_NAME}"

    ALREADY_EXISTS_ERROR = "DiskResourceAlreadyExistsError"
