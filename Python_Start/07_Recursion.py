# # Факториалом числа n (обозначается n!) называется произведение
# # всех натуральных чисел от 1 до n включительно.
#
#
# # пример рекурсивной функции
# def factorial(n):
#     if n == 0:
#         return 1  # условие выхода
#     else:
#         return n * factorial(n - 1)  # рекурсивный вызов
#
#
# # вычисление факториала числа 5
# print(factorial(5))
# -----------------------------------------------------------------------------
# # Числа Фибоначчи — последовательность, в которой первые два числа равны единице,
# # а все последующие — сумме двух предыдущих.
#
#
# def fib(n):
#     if n == 1 or n == 2:  # условие выхода
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)  # рекурсивный вызов
#
#
# index = int(input('Введите номер числа Фибоначчи: '))
# print(fib(index))
# -----------------------------------------------------------------------------
# """
# Ханойская башня является одной из популярных головоломок XIX века.
# Даны три стержня, на один из которых нанизаны восемь колец, причем
# кольца отличаются размером и лежат меньшее на большем. Задача
# состоит в том, чтобы перенести пирамиду из восьми колец за наименьшее
# число ходов на другой стержень. За один раз разрешается переносить
# только одно кольцо, причём нельзя класть большее кольцо на меньшее.
# """
#
#
# def hanoi(n, a, b, c):
#     """Рекурсивный алгоритм решения данной головоломки.
#     Данная функция перекладывает n колец со стержня A
#     на стержень C, используя B как промежуточный
#
#     :param n:  количество колец
#     :param a:  имя первого стержня
#     :param b:  имя второго стержня
#     :param c:  имя третьего стержня
#     :return:   None
#     """
#     if n != 0:  # если количество колец не равно нулю
#         # перенести n - 1 колец из A в B
#         hanoi(n - 1, a, c, b)
#         # перенести одно кольцо из A в C
#         print('Перенести кольцо из', a, 'в', c)
#         # перенести n - 1 колец из B в C
#         hanoi(n - 1, b, a, c)
#
#
# # решение задачи для трёх колец
# hanoi(3, 'A', 'B', 'C')
