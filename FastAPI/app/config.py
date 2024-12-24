from pydantic import BaseSettings


# This is how to setup environmental vars, if no option is given it will
# check and it will do it nicely.
class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_name: str
    database_username: str
    database_password: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"

settings = Settings()