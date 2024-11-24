#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть зашифрованное сообщение

secret_message = [
    'квевтфпп6щ3стмзалтнмаршгб5длгуча',
    'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
    'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
    'ьд5фму3ежородт9г686буиимыкучшсал',
    'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
]

# Расшифровка сообщения
first_word = secret_message[0][3]  # 4-я буква
second_word = secret_message[1][9:13]  # буквы с 10 по 13
third_word = secret_message[2][5:15:2]  # буквы с 6 по 15, через одну
fourth_word = secret_message[3][12:6:-1]  # буквы с 8 по 13 в обратном порядке
fifth_word = secret_message[4][20:15:-1]  # буквы с 17 по 21 в обратном порядке

# Формируем расшифрованное сообщение
decoded_message = f"{first_word} {second_word} {third_word} {fourth_word} {fifth_word}"

# Выводим результат
print(decoded_message)
