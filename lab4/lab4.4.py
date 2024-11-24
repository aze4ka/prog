#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья 
my_family = ['папа', 'мама', 'я', 'дедушка', 'бабушка']

# список списков приблизительного роста членов вашей семьи
my_family_height = [
    ['папа', 180],
    ['мама', 160],
    ['я', 157],
    ['дедушка', 175],
    ['бабушка', 160]
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
father_height = next((height for name, height in my_family_height if name == 'папа'), None)
if father_height is not None:
    print('Рост отца -', father_height, 'см')

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
total_height = sum(height for name, height in my_family_height)
print('Общий рост моей семьи -', total_height, 'см')
