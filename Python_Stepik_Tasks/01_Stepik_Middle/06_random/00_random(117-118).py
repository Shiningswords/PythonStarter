#  -------------------------------------------------------------------------------------------------
#  TASK 117 (Тайный друг)
#  -------------------------------------------------------------------------------------------------
#  Напишите программу, которая случайным образом назначает каждому ученику его тайного друга,
#  который будет вместе с ним решать задачи по программированию.
#  -------------------------------------------------------------------------------------------------

# from random import shuffle
#
# n, names = int(input()), []
# for _ in range(n):
#     names.append(input())
# names_r, flag = names.copy(), False
# shuffle(names_r)
# while True:
#     for i in range(len(names)):
#         if names[i] == names_r[i]:
#             flag = False
#             break
#         else:
#             flag =True
#     if flag:
#         break
#     else:
#         shuffle(names_r)
# for i in range(len(names)):
#     print(f"{names[i]} - {names_r[i]}")

#  -------------------------------------------------------------------------------------------------
#  TASK 117 (Генератор паролей 1)
#  -------------------------------------------------------------------------------------------------
#  Напишите программу, которая с помощью модуля random генерирует nn паролей длиной mm символов,
#  состоящих из строчных и прописных английских букв и цифр, кроме тех, которые легко перепутать между собой:
#  «l» (L маленькое); «I» (i большое); «1» (цифра); «o» и «O» (большая и маленькая буквы); «0» (цифра).
#  -------------------------------------------------------------------------------------------------

# import string
# from random import randrange
#
#
# def generate_password(length):
#     symbs = [i for i in (string.ascii_letters + string.digits) if i not in 'LloO01iI']
#     return ''.join([symbs[randrange(0, len(symbs))] for i in range(length)])
#
#
# def generate_passwords(count, length):
#     for i in range(count):
#         print(generate_password(length))
#
#
# n, m = int(input()), int(input())
# generate_passwords(n, m)

#  -------------------------------------------------------------------------------------------------
#  TASK 118 (Генератор паролей 2)
#  -------------------------------------------------------------------------------------------------
#  Напишите программу, которая с помощью модуля random генерирует nn паролей длиной mm символов,
#  состоящих из строчных и прописных английских букв и цифр, кроме тех, которые легко перепутать между собой:
#  «l» (L маленькое); «I» (i большое); «1» (цифра); «o» и «O» (большая и маленькая буквы); «0» (цифра).
#  Дополнительное условие: в каждом пароле обязательно должна присутствовать хотя бы одна цифра и как минимум по
#  одной букве в верхнем и нижнем регистре.
#  -------------------------------------------------------------------------------------------------

# import string
# from random import randrange
#
#
# def generate_password(length):
#     symbs = [i for i in (string.ascii_letters + string.digits) if i not in 'LloO01iI']
#     res = ''.join([symbs[randrange(0, len(symbs))] for i in range(length)])
#     while True:
#         flag1, flag2, flag3 = False, False, False
#         for c in res:
#             if c in string.digits:
#                 flag1 = True
#             if c in string.ascii_uppercase:
#                 flag2 = True
#             if c in string.ascii_lowercase:
#                 flag3 = True
#         if flag1 and flag2 and flag3:
#             break
#         else:
#             res = ''.join([symbs[randrange(0, len(symbs))] for i in range(length)])
#     return res
#
#
# def generate_passwords(count, length):
#     for i in range(count):
#         print(generate_password(length))
#
#
# n, m = int(input()), int(input())
# generate_passwords(n, m)
