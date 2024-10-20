import numpy as np
from scipy.interpolate import interp1d

print("Хардкод функции")
# Заданные точки для интерполяции
x_points = np.array([1.1, 1.2, 1.3, 1.4, 1.6, 1.7, 1.8])
y_points = np.array([3.0042, 3.3201, 13.6693, 4.4817, 4.953, 5.4739, 6.0496])

# Точки, в которых нужно найти значения функции
x1 = 1.17
x2 = 1.80

# Функция для интерполяции Ньютона
def newton_interpolation(x, x_points, y_points):
    n = len(x_points)
    result = y_points[0]
    for i in range(1, n):
        terms = [x - x_points[j] for j in range(i)]
        result += (divided_difference(x_points[:i], y_points[:i]) * np.prod(terms))
    return result

# Рекурсивная функция для нахождения разделенной разности
def divided_difference(x_values, y_values):
    if len(x_values) == 1:
        return y_values[0]
    return (divided_difference(x_values[1:], y_values[1:]) - divided_difference(x_values[:-1], y_values[:-1])) / (x_values[-1] - x_values[0])

# Вычисляем значения функции в x1 и x2
y1 = newton_interpolation(x1, x_points, y_points)
y2 = newton_interpolation(x2, x_points, y_points)

# Выводим результаты
print("Значение функции в x1:", y1)
print(f"Значение функции в x2: {y2}\n")

print(f"Использование встроенной функции")
# Интерполяция с использованием interp1d
interp_func = interp1d(x_points, y_points, kind='cubic')
y1_interp = interp_func(x1)
y2_interp = interp_func(x2)

# Вывод результатов
print("Значение функции в x1 (SciPy):", y1_interp)
print("Значение функции в x2 (SciPy):", y2_interp)
