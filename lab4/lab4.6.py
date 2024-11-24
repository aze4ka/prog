#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Есть список песен группы Depeche Mode со временем звучания с точностью до долей минут
# Точность указывается в функции round(a, b)
# где a, это число которое надо округлить, а b количество знаков после запятой
# более подробно про функцию round смотрите в документации https://docs.python.org/3/search.html?q=round

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# Распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean'
songs_to_sum_list = ['Halo', 'Enjoy the Silence', 'Clean']
total_time_list = round(sum(song[1] for song in violator_songs_list if song[0] in songs_to_sum_list), 2)
print('Три песни звучат', total_time_list, 'минут')

# Есть словарь песен группы Depeche Mode
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

# Распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
songs_to_sum_dict = ['Sweetest Perfection', 'Policy of Truth', 'Blue Dress']
total_time_dict = round(sum(violator_songs_dict[song] for song in songs_to_sum_dict), 2)
print('А другие три песни звучат', total_time_dict, 'минут')
