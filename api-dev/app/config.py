from pydantic import BaseSettings


class Setting(BaseSettings):
    acces_token_expire_minutes: int
    secret_key: str
    algorithm: str
    db_post: str
    db_host: str
    db_psw: str
    db_un: str

    class Config:
        env_file = '.env'


setting = Setting()
