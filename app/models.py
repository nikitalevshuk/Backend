from typing import Annotated

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base

# эта переменная позднее указывается в качестве типа данных, но еще и содержит в себе информацию о колонке, что сокращает код, при этом на информацию о колонке из перемен-
# ной можно наслаивать еще и свои параметры mapped_column
# ПРИМЕЧАНИЕ - ТУТ СТОИЛО БЫ ДОБАВИТЬ ТИПИЗАЦИЮ ИЗ РАЗРЯДА STRING_256 И ТОМУ ПОДОБНОЕ
intpk = Annotated[int, mapped_column(primary_key=True)]

# создаю таблицу услуг
class ServicesTable(Base):
    __tablename__ = "services"
    id: Mapped[intpk] 
    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[int]
    duration: Mapped[int]

# создаю таблицу работников
class SpecialistsTable(Base):
    __tablename__ = "specialists"
    id: Mapped[intpk]
    name: Mapped[str]

# создаю таблицу заказов
class OrdersTable(Base):
    __tablename__ = "orders"
    id: Mapped[intpk]
    name: Mapped[str] 
    service_id: Mapped[str] = mapped_column(ForeignKey("services.id", ondelete="CASCADE"))
    specialist_id: Mapped[str] = mapped_column(ForeignKey("specialists.id", ondelete="CASCADE"))