from config.base_config import Config

WP_POSTS_ENDPOINT = f"{Config.WP_REST_PREFIX}/wp/v2/posts"

YA_DISK_ENDPOINT = "/v1/disk"


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
