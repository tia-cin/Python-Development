from pydantic import BaseSettings


class Settings(BaseSettings):
    access_token_expire_minutes: int
    secret_key: str
    algorithm: str
    db_port: str
    db_host: str
    db_name: str
    db_psw: str
    db_un: str

    class Config:
        env_file = '.env'


setting = Settings()
