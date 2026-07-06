import re
import requests


def parse_response(response: requests.Response) -> tuple[int, dict]:
    return response.status_code, response.json()


def find_resource_in_items(items: list[dict], original_name: str) -> str | None:
    pattern = re.compile(rf"^{re.escape(original_name)}(_[a-f0-9]+)?$")
    for item in items:
        if pattern.match(item["name"]):
            return item["path"][7:]
    return None
