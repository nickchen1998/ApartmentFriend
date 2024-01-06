from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent


class EnvSettings(BaseSettings):
    USE_SQLITE: bool = False
    SECRET_KEY: str = None
    DB_NAME: str = "aptfriend"

    MARIA_SUPERUSER: str = "root"
    MARIA_SUPERUSER_PASSWORD: str = "1234"
    MARIA_HOST: str = "localhost"
    MARIA_PORT: str = "3306"

    REDIS_URL: str = "redis://ah-redis:6379/0"

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / '.env',
        env_file_encoding='utf-8'
    )
