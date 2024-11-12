from app.database import sync_engine, async_engine, session_factory, async_session_factory, Base
from app.models import ServicesTable, OrdersTable, SpecialistsTable
from sqlalchemy import select
# объявляю класс чтобы сгребать в него функции относящиеся к синхронным запросам с ORM таблицами
class SyncOrm:
    # реализую статический метод для создания всех таблиц которые относятся к классу Base
    @staticmethod
    def create_tables():
        sync_engine.echo = True
        Base.metadata.drop_all(sync_engine)
        Base.metadata.create_all(sync_engine)
        sync_engine.echo = True

    @staticmethod
    def insert_tables():
        with session_factory() as session:
            # Создаём услуги
            service_one = ServicesTable(
                name='Стрижка',
                description='Классическая короткая стрижка',
                price=40,
                duration=60,
            )
            service_two = ServicesTable(
                name='Бритье',
                description='Услуга бритья опасной бритвой',
                price=20,
                duration=30,
            )

            # Создаём специалистов
            specialist_one = SpecialistsTable(
                name='Петька Гвоздиков',
            )
            specialist_two = SpecialistsTable(
                name='Руслан Гительман',
            )

            # Добавляем записи услуг и специалистов в сессию и фиксируем их
            session.add_all([service_one, service_two, specialist_one, specialist_two])
            session.flush()  # Теперь у них есть id

            # Теперь создаём заказы с использованием внешних ключей
            order_one = OrdersTable(
                name='Михаил',
                service_id=service_one.id,
                specialist_id=specialist_one.id                                          
            )

            order_two = OrdersTable(
                name='Никита',
                service_id=service_two.id,
                specialist_id=specialist_two.id
            )

            # Добавляем заказы в сессию и фиксируем
            session.add_all([order_one, order_two])
            session.commit()


    # @staticmethod
    # def select_workers():
    #     with session_factory() as session:
    #         # worker_id = 1
    #         # worker_jack = session.get(WorkerTable, worker_id)
    #         query = select(WorkerTable)
    #         result = session.execute(query)
    #         workers = result.scalars().all()
    #         print(f"{workers=}")

    # @staticmethod
    # def update_worker(worker_id:int = 2, new_username:str = "Misha"):
    #     with session_factory() as session:
    #         worker_michael = session.get(WorkerTable, worker_id)
    #         worker_michael.username = new_username
    #         session.commit()

            
        