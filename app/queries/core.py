from app.models import metadata_obj, workers_table  
from app.database import sync_engine
from sqlalchemy import text, insert, select, update

# создал класс с целью удобного поднесения функций под одну гребенку(в моем случае синхронные функции для работы с не ORM таблицами)
class SyncCore:
    # статический метод для создания всех таблиц которые записаны в metadata_obj(отличается от Base.metadata)
    @staticmethod
    def create_tables():
        sync_engine.echo = False
        metadata_obj.drop_all(sync_engine)
        metadata_obj.create_all(sync_engine)
        sync_engine.echo = True
    
    # статический метод для вставки работника в таблицу
    @staticmethod
    def insert_worker():
        with sync_engine.connect() as conn:
            stmt = insert(workers_table).values(
                [
                    {"username": "Jack"},
                    {"username": "Michael"}
                ]
            )
            conn.execute(stmt)
            conn.commit()
    
    # статический метод для вывода работников из таблицы
    @staticmethod
    def select_workers():
        with sync_engine.connect() as conn:
            query = select(workers_table)
            result = conn.execute(query)
            print(result.all())

    # статический метод для обновления информации о работнике
    @staticmethod
    def update_worker(worker_id:int = 2, new_username:str = 'Nikita'):
        with sync_engine.connect() as conn:
            stmt = (
                update(workers_table).
                filter_by(id = worker_id)
            )
            conn.execute(stmt)
            conn.commit()
            
        

