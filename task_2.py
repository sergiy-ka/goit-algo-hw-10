# Завдання 2. Обчислення визначеного інтеграла.

import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integrate

# Метод Монте-Карло


def monte_carlo_integrate(func, a, b, y_min, y_max, num_points):
    x = np.random.uniform(a, b, num_points)
    y = np.random.uniform(y_min, y_max, num_points)
    under_curve = np.sum(y < func(x))
    # print(under_curve)
    area = (b - a) * (y_max - y_min) * (under_curve / num_points)
    return area

# Визначення функції та межі інтегрування


def f(x):
    return x ** 2


a = 0  # Нижня межа
b = 2  # Верхня межа

y_min = a
y_max = f(b)

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.axhline(y=f(b), color='gray', linestyle='--')

ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()


if __name__ == "__main__":
    # Обчислення інтеграла (quad)
    result, err = integrate.quad(f, a, b)
    # Обчислення інтеграла (методом Монте-Карло) при різних значеннях num_points
    monte_carlo_data = {}
    num_points = 10
    for i in range(1, 6):
        num_points = num_points * 10
        mc_result = monte_carlo_integrate(f, a, b, y_min, y_max, num_points)
        monte_carlo_data[num_points] = mc_result
    # Виведення результатів
    print("Таблиця результатів обчислення інтеграла методом Монте-Карло:")
    print(f"| {'-'*25:^25} | {'-'*25:^25} |")
    print(f"| {'Кількість точок':^25} | {'Площа':^25} |")
    print(f"| {'-'*25:^25} | {'-'*25:^25} |")
    for key, value in monte_carlo_data.items():
        print(f"| {key:^25} | {value:^25} |")
    print(f"| {'-'*25:^25} | {'-'*25:^25} |")
    print(
        f"Інтеграл: quad ({result}), Монте-Карло ({monte_carlo_data[num_points]})")
    # Висновок
    print(f"""Висновок: Метод Монте-Карло дає точніший результат при збільшенні кількості точок.""")
