from datetime import datetime


services = {
    1:{"id": 1, "name": "Стрижка", "description":"Классическая короткая стрижка", "price": 40, "duration": 60},
    2:{"id": 2, "name": "Бритье", "description":"Услуга бритья опасной бритвой", "price": 20, "duration": 30}
}

specialists = {
    1:{"id": 1, "name": "Петька Гвоздиков"},
    2:{"id": 2, "name": "Стас Шило"}
}

orders = {
    1:{"id":1, "name": "Михаил", "service_id": 1, "specialist_id": 1, "time": datetime.strptime("2024-10-30 15:30:00", "%Y-%m-%d %H:%M:%S")},
    1:{"id":2, "name": "Александр", "service_id": 2, "specialist_id": 2, "time": datetime.strptime("2024-10-28 14:30:00", "%Y-%m-%d %H:%M:%S")}
}