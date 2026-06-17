import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    WP_BASE_URL: str = os.getenv("WP_BASE_URL", "http://localhost:8000")
    WP_REST_PREFIX: str = "/index.php?rest_route="
    WP_USER: str = os.getenv("WP_USER", "")
    WP_PASSWORD: str = os.getenv("WP_PASSWORD", "")

    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: int = int(os.getenv("DB_PORT", "3306"))
    DB_NAME: str = os.getenv("DB_NAME", "wordpress")
    DB_USER: str = os.getenv("DB_USER", "wordpress")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "wordpress")
