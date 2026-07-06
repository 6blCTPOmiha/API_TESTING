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

    def insert_post(self, content: str, title: str, status: str = "publish") -> int:
        self._cursor.execute(
            """
            INSERT INTO wp_posts (
            post_author, post_date, post_date_gmt, post_content,
            post_title, post_excerpt, post_status, comment_status, ping_status,
            post_name, to_ping, pinged, post_modified, post_modified_gmt,
            post_content_filtered, post_type, post_mime_type)
            VALUES (
            1, '2026-06-02 20:11:34', '2026-06-02 17:11:34', %s,
            %s, '', %s, 'open', 'open', 
            %s, '', '', '2026-06-13 23:00:02', '2026-06-13 20:00:02', 
            '', 'post', '')
            """,
            (content, title, status, title.lower().replace(" ", "-")),
        )
        self._connection.commit()
        return self._cursor.lastrowid

    def delete_post_by_id(self, post_id: int) -> None:
        self._cursor.execute(
            "DELETE FROM wp_posts WHERE id = %s OR post_parent = %s",
            (post_id, post_id),
        )
        self._connection.commit()

    def close_connection(self) -> None:
        self._cursor.close()
        self._connection.close()
