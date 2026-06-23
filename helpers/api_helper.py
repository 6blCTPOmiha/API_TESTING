import requests

from config.base_config import Config


class ApiHelper:

    def __init__(self, base_url: str, auth: tuple | None = None, token: str | None = None):
        self._base_url = base_url.rstrip("/")
        self._session = requests.Session()

        if auth:
            self._session.auth = auth
        if token:
            self._session.headers.update({'Authorization': f'{token}'})

        self._session.headers.update({"Content-Type": "application/json"})

    def _build_url(self, endpoint: str) -> str:
        return f"{self._base_url}{endpoint}"

    def get(self, endpoint: str, **kwargs) -> requests.Response:
        return self._session.get(self._build_url(endpoint), **kwargs)

    def post(self, endpoint: str, json: dict | None = None, **kwargs) -> requests.Response:
        return self._session.post(self._build_url(endpoint), json=json, **kwargs)

    def patch(self, endpoint: str, json: dict | None = None, **kwargs) -> requests.Response:
        return self._session.patch(self._build_url(endpoint), json=json, **kwargs)

    def put(self, endpoint: str, json: dict | None = None, **kwargs) -> requests.Response:
        return self._session.put(self._build_url(endpoint), json=json, **kwargs)

    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        return self._session.delete(self._build_url(endpoint), **kwargs)

    def close(self) -> None:
        self._session.close()


def get_wp_client() -> ApiHelper:
    return ApiHelper(
        base_url=Config.WP_BASE_URL,
        auth=(Config.WP_USER, Config.WP_PASSWORD),
    )
