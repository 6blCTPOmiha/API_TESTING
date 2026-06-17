import pytest

from helpers.db_helper import DbHelper
from helpers.wordpress_api import WordPressApi



@pytest.fixture(scope="session")
def wp_api() -> WordPressApi:
    client = WordPressApi()
    yield client
    client.close()


@pytest.fixture(scope="session")
def db() -> DbHelper:
    helper = DbHelper()
    yield helper
    helper.close_connection()
