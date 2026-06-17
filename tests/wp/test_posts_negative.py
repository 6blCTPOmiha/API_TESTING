import allure

from data.test_data import PostData


@allure.epic("WordPress API")
@allure.feature("Posts")
class TestPostsNegative:

    @allure.story("Создание поста")
    @allure.title("TC-ADD-02: POST /wp/v2/posts только со статусом, без title и content")
    def test_create_post_status_only(self, wp_api):

        response = wp_api.create_post(PostData.STATUS_ONLY_PAYLOAD)
        assert response.status_code == 400, "Ожидался статус 400 Bad Request"
        assert response.json()["message"] == PostData.EMPTY_CONTENT_ERROR, "Сообщение об ошибке не корректное"

    @allure.story("Редактирование поста")
    @allure.title("TC-EDT-02: PUT /wp/v2/posts/1 с пустыми title и content")
    def test_update_post_empty_fields(self, wp_api, post_for_update):

        post_id = post_for_update

        response = wp_api.update_post(post_id, PostData.EMPTY_FIELDS_PAYLOAD)
        assert response.status_code == 400, "Ожидался статус 400 Bad Request"
        assert response.json()["message"] == PostData.EMPTY_CONTENT_ERROR, "Сообщение об ошибке не корректное"


    @allure.story("Удаление поста")
    @allure.title("TC-DEL-02: DELETE /wp/v2/posts/99999 для несуществующего поста")
    def test_delete_post_not_existing(self, wp_api):

        response = wp_api.delete_post(99999)
        assert response.status_code == 404, "Ожидался статус 404 Not Found"
        assert response.json()["message"] == PostData.INVALID_ID_ERROR, "Сообщение об ошибке не корректное"


    @allure.story("Получение поста")
    @allure.title("TC-GET-03: GET /wp/v2/posts/{id} для несуществующего поста")
    def test_get_post_not_existing(self, wp_api):
        response = wp_api.get_post(99999)
        assert response.status_code == 404, "Ожидался статус 404 Not Found"
        assert response.json()["message"] == PostData.INVALID_ID_ERROR
