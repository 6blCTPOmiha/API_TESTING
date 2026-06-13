import allure
import pytest

from data.test_data import WP_POSTS_ENDPOINT, PostData


@allure.epic("WordPress API")
@allure.feature("Posts")
class TestPostsCreate:

    @allure.story("Создание поста")
    @allure.title("TC-ADD-01: POST /wp/v2/posts с валидными данными")
    def test_create_post_valid_data(self, wp_client, db):

        response = wp_client.post(WP_POSTS_ENDPOINT, json=PostData.VALID_PAYLOAD)
        assert response.status_code == 201, "Ожидался статус 201 Created"

        body = response.json()
        assert "id" in body, "В ответе отсутствует поле id"

        post_id = body["id"]
        db_post = db.get_post_by_id(post_id)
        assert db_post is not None, f"Пост с id={post_id} не найден в БД"
        assert db_post["post_title"] == PostData.VALID_TITLE, "post_title не корректный"
        assert db_post["post_content"] == PostData.VALID_CONTENT, "post_content не корректный"
        assert db_post["post_status"] == PostData.VALID_STATUS, "post_status не корректный"

    @allure.story("Создание поста")
    @allure.title("TC-ADD-02: POST /wp/v2/posts только со статусом, без title и content")
    def test_create_post_status_only(self, wp_client):

        response = wp_client.post(WP_POSTS_ENDPOINT, json=PostData.STATUS_ONLY_PAYLOAD)
        assert response.status_code == 400, "Ожидался статус 400 Bad Request"
        assert response.json()["message"] == PostData.EMPTY_CONTENT_ERROR, "Сообщение об ошибке не корректное"


@allure.epic("WordPress API")
@allure.feature("Posts")
class TestPostsUpdate:

    @allure.story("Редактирование поста")
    @allure.title("TC-EDT-01: PUT /wp/v2/posts/1 с валидными данными")
    def test_update_post_valid_data(self, wp_client, db):

        if not db.check_post_exists(1):
            pytest.skip("Предусловие не выполнено: в БД отсутствует post с id=1")

        response = wp_client.put(f"{WP_POSTS_ENDPOINT}/1", json=PostData.UPDATED_PAYLOAD)
        assert response.status_code == 200, "Ожидался статус 200 OK"
        assert response.json()["id"] == 1, "id в ответе не корректный"

        db_post = db.get_post_by_id(1)
        assert db_post["post_title"] == PostData.UPDATED_TITLE, "post_title не корректный"
        assert db_post["post_content"] == PostData.UPDATED_CONTENT, "post_content не корректный"

    @allure.story("Редактирование поста")
    @allure.title("TC-EDT-02: PUT /wp/v2/posts/1 с пустыми title и content")
    def test_update_post_empty_fields(self, wp_client, db):

        if not db.check_post_exists(1):
            pytest.skip("Предусловие не выполнено: в БД отсутствует post с id=1")

        response = wp_client.put(f"{WP_POSTS_ENDPOINT}/1", json=PostData.EMPTY_FIELDS_PAYLOAD)
        assert response.status_code == 400, "Ожидался статус 400 Bad Request"
        assert response.json()["message"] == PostData.EMPTY_CONTENT_ERROR, "Сообщение об ошибке не корректное"


@allure.epic("WordPress API")
@allure.feature("Posts")
class TestPostsDelete:

    @allure.story("Удаление поста")
    @allure.title("TC-DEL-01: DELETE /wp/v2/posts/9")
    def test_delete_post_existing(self, wp_client, db):

        post_status = db.get_post_status(9)
        if post_status is None:
            pytest.skip("Предусловие не выполнено: в БД отсутствует post с id=9")
        if post_status == "trash":
            pytest.skip("Предусловие не выполнено: post с id=9 уже находится в корзине")

        response = wp_client.delete(f"{WP_POSTS_ENDPOINT}/9")
        assert response.status_code == 200, "Ожидался статус 200 OK"
        assert db.get_post_status(9) == "trash", "Пост должен быть перемещён в корзину"


    @allure.story("Удаление поста")
    @allure.title("TC-DEL-02: DELETE /wp/v2/posts/999 для несуществующего поста")
    def test_delete_post_not_existing(self, wp_client):

        response = wp_client.delete(f"{WP_POSTS_ENDPOINT}/999")
        assert response.status_code == 404, "Ожидался статус 404 Not Found"
        assert response.json()["message"] == PostData.INVALID_ID_ERROR, "Сообщение об ошибке не корректное"
