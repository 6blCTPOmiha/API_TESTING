import pytest

from data.test_data import PostData


@pytest.fixture
def delete_post_after(db):
    post_ids = []
    yield post_ids
    for post_id in post_ids:
        db.delete_post_by_id(post_id)


@pytest.fixture
def post_for_update(wp_api, db):
    response = wp_api.create_post(PostData.VALID_PAYLOAD)
    assert response.status_code == 201, "Фикстура: не удалось создать пост для редактирования"
    post_id = response.json()["id"]
    yield post_id
    db.delete_post_by_id(post_id)


@pytest.fixture
def post_for_delete(wp_api, db):
    response = wp_api.create_post(PostData.VALID_PAYLOAD)
    assert response.status_code == 201, "Фикстура: не удалось создать пост для удаления"
    post_id = response.json()["id"]
    yield post_id
    db.delete_post_by_id(post_id)


@pytest.fixture
def inserted_post(db):
    post_id = db.insert_post(
        content=PostData.VALID_CONTENT,
        title=PostData.VALID_TITLE,
        status=PostData.VALID_STATUS,
    )
    yield post_id
    db.delete_post_by_id(post_id)
