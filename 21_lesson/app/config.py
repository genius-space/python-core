import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

current_script_path = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(current_script_path, '..', 'database.env')

load_dotenv(dotenv_path)


class TestSettings():
    DB_HOST_TEST: str = os.environ.get("DB_HOST_TEST")
    DB_PORT_TEST: str = os.environ.get("DB_PORT_TEST")
    DB_NAME_TEST: str = os.environ.get("DB_NAME_TEST")
    DB_USER_TEST: str = os.environ.get("DB_USER_TEST")
    DB_PASS_TEST: str = os.environ.get("DB_PASS_TEST")
    DATABASE_URL: str = f"postgresql+asyncpg://{DB_USER_TEST}:{DB_PASS_TEST}@{DB_HOST_TEST}:{DB_PORT_TEST}/{DB_NAME_TEST}"


class ProdSettings():
    DB_HOST: str = os.environ.get("POSTGRES_HOST")
    DB_PORT: str = os.environ.get("POSTGRES_PORT")
    DB_NAME: str = os.environ.get("POSTGRES_DB")
    DB_USER: str = os.environ.get("POSTGRES_USER")
    DB_PASS: str = os.environ.get("POSTGRES_PASSWORD")
    DATABASE_URL: str = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

def get_settings():
    env = os.getenv("ENVIRONMENT", "Not database").lower()
    if env == "testing":
        return TestSettings()
    elif env == "production":
        return ProdSettings()
    else:
        raise ValueError(f"Unknown environment: {env}")


settings = get_settings()
