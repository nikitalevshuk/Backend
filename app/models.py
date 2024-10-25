from pydantic import HttpUrl


services = {
    1:{"id": 1, "name": "Стрижка", "description":"Классическая короткая стрижка", "price": 40, "duration": 60},
    2:{"id": 2, "name": "Бритье", "description":"Услуга бритья опасной бритвой", "price": 20, "duration": 30}
}

specialists = {
    1:{"id": 1, "name": "Петька Гвоздиков"},
    2:{"id": 2, "name": "Стас Шило"}
}