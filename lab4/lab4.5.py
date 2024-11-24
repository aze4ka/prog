#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# есть список животных в зоопарке
zoo = ['lion', 'kangaroo', 'elephant', 'monkey']

# посадите медведя (bear) между львом и кенгуру
zoo.insert(1, "bear")
print("Список животных после посадки медведя:", zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark']
for bird in birds:
    zoo.append(bird)
print("Список животных после добавления птиц:", zoo)

# уберите слона
zoo.remove("elephant")
print("Список животных после удаления слона:", zoo)

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
lion_index = zoo.index("lion") + 1  # +1 для удобства пользователя
lark_index = zoo.index("lark") + 1   # +1 для удобства пользователя
print(f"Лев сидит в клетке номер {lion_index}, жаворонок сидит в клетке номер {lark_index}.")
