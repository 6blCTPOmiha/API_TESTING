import requests

from config.base_config import Config
from helpers.api_helper import ApiHelper
from data.test_data import WP_POSTS_ENDPOINT


class WordPressApi(ApiHelper):

    def __init__(self):
        super().__init__(
            base_url=Config.WP_BASE_URL,
            auth=(Config.WP_USER, Config.WP_PASSWORD),
        )

    def create_post(self, payload: dict) -> requests.Response:
        return self.post(WP_POSTS_ENDPOINT, json=payload)

    def update_post(self, post_id: int, payload: dict) -> requests.Response:
        return self.patch(f"{WP_POSTS_ENDPOINT}/{post_id}", json=payload)

    def delete_post(self, post_id: int) -> requests.Response:
        return self.delete(f"{WP_POSTS_ENDPOINT}/{post_id}")
