from pydantic import BaseSettings, validator


class Settings(BaseSettings):
    SECRET_KEY: str
    DATABASE_MYSQL_URL: str
    BACKEND_CORS_ORIGINS: str

    @validator("BACKEND_CORS_ORIGINS")
    def assemble_cors_origins(cls, v: str):
        return [i.strip() for i in v.split(",")]

    class Config:
        env_file = '.env'


settings = Settings()
