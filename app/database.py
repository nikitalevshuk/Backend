from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from app.config import settings

# создаю синхронный движок(для этого импортирую из sqlalchemy create_engine и передаю туда ссылку на БД и другие разные параметры)
sync_engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True
)

# создаю асинхронный движок, отличие только в том что импортирую из sqlalchemy.ext.asyncio create_async_engine 
async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=True
)

# создаю класс Base который наследуется от DeclarativeBase, суть в том что для создания таблицы используя ORM мне нужно унаследовать эти таблицы от босса,
# который ведет записи про то, что у кого есть (Base.metadata), потом метадата будет нужна для того, чтобы по ней создавать таблицы в БД
class Base(DeclarativeBase):
    pass

# создаю класс сессий для того, чтобы скоротить код. без этого пришлось бы писать больше кода + я тот дурацкий синтаксис не помню
session_factory = sessionmaker(sync_engine)
async_session_factory = async_sessionmaker(async_engine)
