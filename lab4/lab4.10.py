#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров
goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.
store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе

# Лампы
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Столы
table_code = goods['Стол']
tables_items = store[table_code]
tables_quantity = sum(item['quantity'] for item in tables_items)
tables_cost = sum(item['quantity'] * item['price'] for item in tables_items)
print('Стол -', tables_quantity, 'шт, стоимость', tables_cost, 'руб')

# Диваны
sofa_code = goods['Диван']
sofas_items = store[sofa_code]
sofas_quantity = sum(item['quantity'] for item in sofas_items)
sofas_cost = sum(item['quantity'] * item['price'] for item in sofas_items)
print('Диван -', sofas_quantity, 'шт, стоимость', sofas_cost, 'руб')

# Стулья
chair_code = goods['Стул']
chairs_items = store[chair_code]
chairs_quantity = sum(item['quantity'] for item in chairs_items)
chairs_cost = sum(item['quantity'] * item['price'] for item in chairs_items)
print('Стул -', chairs_quantity, 'шт, стоимость', chairs_cost, 'руб')
