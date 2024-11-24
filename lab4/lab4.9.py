#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь магазинов с распродажами
shops = {
    'ашан': [
        {'name': 'печенье', 'price': 10.99},
        {'name': 'конфеты', 'price': 34.99},
        {'name': 'карамель', 'price': 45.99},
        {'name': 'пирожное', 'price': 67.99}
    ],
    'пятерочка': [
        {'name': 'печенье', 'price': 9.99},
        {'name': 'конфеты', 'price': 32.99},
        {'name': 'карамель', 'price': 46.99},
        {'name': 'пирожное', 'price': 59.99}
    ],
    'магнит': [
        {'name': 'печенье', 'price': 11.99},
        {'name': 'конфеты', 'price': 30.99},
        {'name': 'карамель', 'price': 41.99},
        {'name': 'пирожное', 'price': 62.99}
    ],
}

# Создайте словарь цен на продукты
sweets = {}

# Заполняем словарь sweets на основе данных из shops
for shop, products in shops.items():
    for product in products:
        name = product['name']
        price = product['price']
        
        # Если сладость еще не добавлена, создаем новую запись
        if name not in sweets:
            sweets[name] = []
        
        # Добавляем магазин и цену в список
        sweets[name].append({'shop': shop, 'price': price})

# Указываем только по 2 магазина с минимальными ценами
for sweet, stores in sweets.items():
    # Сортируем магазины по цене
    sorted_stores = sorted(stores, key=lambda x: x['price'])
    
    # Оставляем только два магазина с минимальными ценами
    top_stores = sorted_stores[:2]
    
    print(f"{sweet}:")
    for store in top_stores:
        print(f" - {store['shop']}: {store['price']:.2f}")
