import mysql.connector

from config.base_config import Config


class DbHelper:

    def __init__(self):
        self._connection = mysql.connector.connect(
            ssl_disabled=True,
            host=Config.DB_HOST,
            port=Config.DB_PORT,
            database=Config.DB_NAME,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
        )
        self._cursor = self._connection.cursor(dictionary=True)

    def get_post_by_id(self, post_id: int) -> dict | None:
        self._connection.commit()
        self._cursor.execute(
            "SELECT * FROM wp_posts WHERE ID = %s",
            (post_id,),
        )
        return self._cursor.fetchone()

    def check_post_exists(self, post_id: int) -> bool:
        return self.get_post_by_id(post_id) is not None

    def get_post_status(self, post_id: int) -> str | None:
        row = self.get_post_by_id(post_id)
        return row["post_status"] if row else None

    def get_post_title(self, post_id: int) -> str | None:
        row = self.get_post_by_id(post_id)
        return row["post_title"] if row else None

    def delete_post_by_id(self, post_id: int) -> None:
        self._cursor.execute(
            "DELETE FROM wp_posts WHERE id = %s OR post_parent = %s",
            (post_id, post_id),
        )
        self._connection.commit()

    def close_connection(self) -> None:
        self._cursor.close()
        self._connection.close()
