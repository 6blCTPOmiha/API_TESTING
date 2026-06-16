import allure

from data.test_data import PostData


@allure.epic("WordPress API")
@allure.feature("Posts")
class TestPostsPositive:

    @allure.story("Создание поста")
    @allure.title("TC-ADD-01: POST /wp/v2/posts с валидными данными")
    def test_create_post_valid_data(self, wp_api, db, delete_post_after):

        response = wp_api.create_post(PostData.VALID_PAYLOAD)
        assert response.status_code == 201, "Ожидался статус 201 Created"

        body = response.json()
        assert "id" in body, "В ответе отсутствует поле id"

        post_id = body["id"]
        delete_post_after.append(post_id)
        db_post = db.get_post_by_id(post_id)
        assert db_post is not None, f"Пост с id={post_id} не найден в БД"
        assert db_post["post_title"] == PostData.VALID_TITLE, "post_title не корректный"
        assert db_post["post_content"] == PostData.VALID_CONTENT, "post_content не корректный"
        assert db_post["post_status"] == PostData.VALID_STATUS, "post_status не корректный"


    @allure.story("Редактирование поста")
    @allure.title("TC-EDT-01: PUT /wp/v2/posts/1 с валидными данными")
    def test_update_post_valid_data(self, wp_api, db, post_for_update):

        post_id = post_for_update
        response = wp_api.update_post(post_id, PostData.UPDATED_PAYLOAD)
        assert response.status_code == 200, "Ожидался статус 200 OK"
        assert response.json()["id"] == post_id, "id в ответе не корректный"

        db_post = db.get_post_by_id(post_id)
        assert db_post["post_title"] == PostData.UPDATED_TITLE, "post_title не корректный"
        assert db_post["post_content"] == PostData.UPDATED_CONTENT, "post_content не корректный"


    @allure.story("Удаление поста")
    @allure.title("TC-DEL-01: DELETE /wp/v2/posts/9")
    def test_delete_post_existing(self, wp_api, db, post_for_delete):

        post_id = post_for_delete
        response = wp_api.delete_post(post_id)
        assert response.status_code == 200, "Ожидался статус 200 OK"
        assert db.get_post_status(post_id) == "trash", "Пост должен быть перемещён в корзину"
