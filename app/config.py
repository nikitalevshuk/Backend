# основное или единственное назначение BaseSettings так это то, что это оболочка класса в котором можно параметрами можно загрузить переменные окружения, которые 
# берутся из файла который указывается в model_config = SettingsConfigDict(env_file = "")
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    
    DB_HOST:str
    DB_PORT:int
    DB_USER:str
    DB_PASS:str
    DB_NAME:str

    @property
    def DATABASE_URL_psycopg(self):
        return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    @property
    def DATABASE_URL_asyncpg(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file='.env')

# создаю объект класса Settings, чтобы потом передавать геттеры в параметр url при создании движка БД
settings = Settings()
