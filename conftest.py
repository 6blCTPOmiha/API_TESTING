import pytest

from helpers.api_helper import get_wp_client, ApiHelper
from helpers.db_helper import DbHelper


@pytest.fixture(scope="session")
def wp_client() -> ApiHelper:
    client = get_wp_client()
    yield client
    client.close()


@pytest.fixture(scope="session")
def db() -> DbHelper:
    helper = DbHelper()
    yield helper
    helper.close_connection()

