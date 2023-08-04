from typing import Any

from sqlalchemy.engine import URL

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Postgresql settings
    POSTGRES_SERVER: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    # Postgresql settings
    TEST_POSTGRES_SERVER: str
    TEST_POSTGRES_PORT: int
    TEST_POSTGRES_USER: str
    TEST_POSTGRES_PASSWORD: str
    TEST_POSTGRES_DB: str

    # Redis settings
    REDIS_HOST: str
    REDIS_PORT: str
    REDIS_PATH: str

    CONTACT_PATH: str

    model_config = SettingsConfigDict(env_file=".env")

    @property
    def uri_db_connection(self) -> Any:
        return URL.create(
            "postgresql+psycopg",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_SERVER,
            database=self.POSTGRES_DB,
        )

    @property
    def uri_test_db_connection(self) -> Any:
        return URL.create(
            "postgresql+psycopg",
            username=self.TEST_POSTGRES_USER,
            password=self.TEST_POSTGRES_PASSWORD,
            host=self.TEST_POSTGRES_SERVER,
            database=self.TEST_POSTGRES_DB,
        )

    @property
    def uri_redis_connection(self) -> Any:
        return f'redis://{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_PATH}'


settings = Settings()
