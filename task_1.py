# Завдання 1. Оптимізація виробництва

import pulp

# Модель
model = pulp.LpProblem("Maximize production", pulp.LpMaximize)

# Змінні
L = pulp.LpVariable("Лимонад", lowBound=0, cat='Integer')
J = pulp.LpVariable("Фруктовий сік", lowBound=0, cat='Integer')

# Функція
model += L + J, "Total production"

# Обмеження
model += 2 * L + J <= 100, "Вода"
model += L <= 50, "Цукор"
model += L <= 30, "Лимонний сік"
model += 2 * J <= 40, "Фруктове пюре"

model.solve()

# Результати
print(f"Status: {model.status}, {pulp.LpStatus[model.status]}")
print(
    f"""Максимально можлива кількість вироблених продуктів "Лимонад" та "Фруктовий сік":
    - Лимонад: {L.value()}, 
    - Фруктовий сік: {J.value()}.""")
