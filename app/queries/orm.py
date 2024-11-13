from app.database import sync_engine, session_factory, async_session_factory, Base
from app.models import ServicesTable, OrdersTable, SpecialistsTable

from sqlalchemy import select

# объявляю класс чтобы сгребать в него функции относящиеся к синхронным запросам с ORM таблицами
class SyncOrm:
    # реализую статический метод для создания всех таблиц которые относятся к классу Base
    @staticmethod
    def create_tables():
        Base.metadata.drop_all(sync_engine)
        Base.metadata.create_all(sync_engine)

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

class AsyncOrm:

    @staticmethod
    async def insert_tables():
        async with async_session_factory() as session:
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
            await session.flush()  # Теперь у них есть id

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
            await session.commit()


            
        