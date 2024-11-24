#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть значение радиуса круга
radius = 42

# Выведите на консоль значение площади этого круга с точностью до 4-х знаков после запятой
# Формула площади круга: S = π * r^2
pi = 3.1415926
area = round(pi * radius ** 2, 4)
print(area)

# Далее, пусть есть координаты точки
point_1 = (23, 34)  # где 23 - координата x, 34 - координата y

# Функция для проверки, находится ли точка внутри круга
def is_point_inside_circle(point):
    # Определяем расстояние от точки до начала координат (0, 0)
    distance = (point[0] ** 2 + point[1] ** 2) ** 0.5
    # Возвращаем True, если расстояние меньше или равно радиусу, иначе False
    return distance <= radius

# Проверяем первую точку
print(is_point_inside_circle(point_1))

# Аналогично для другой точки
point_2 = (30, 30)

# Проверяем вторую точку
print(is_point_inside_circle(point_2))
