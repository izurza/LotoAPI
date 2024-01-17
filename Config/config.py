from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    api_key: str
    sql_server: str
    sql_database: str
    sql_user: str
    sql_password: str
    
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

settings = Settings()