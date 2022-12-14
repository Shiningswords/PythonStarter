#  -------------------------------------------------------------------------------------------------
#  TASK 92 (Python is awesome)
#  -------------------------------------------------------------------------------------------------
#  Напишите программу, которая выводит слова «Python is awesome!» (без кавычек) 10 раз.
#  -------------------------------------------------------------------------------------------------

# for i in range(10):
#     print("Python is awesome!")

#  -------------------------------------------------------------------------------------------------
#  TASK 93 (Повторяй за мной 1)
#  -------------------------------------------------------------------------------------------------
#  Дано предложение и количество раз которое его надо повторить.
#  Напишите программу, которая повторяет данное предложение нужное количество раз.
#  -------------------------------------------------------------------------------------------------

# text, num = input(), int(input())
# for i in range(num):
#     print(text)

#  -------------------------------------------------------------------------------------------------
#  TASK 94 (Последовательность символов)
#  -------------------------------------------------------------------------------------------------
#  Напишите программу, которая использует ровно три цикла for для печати следующей последовательности символов:
# AAA
# AAA
# AAA
# AAA
# AAA
# AAA
# BBBB
# BBBB
# BBBB
# BBBB
# BBBB
# E
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# G
#  -------------------------------------------------------------------------------------------------

# for i in range(6):
#     print("AAA")
# for i in range(5):
#     print("BBBB")
# print("E")
# for i in range(9):
#     print("TTTTT")
# print("G")

#  -------------------------------------------------------------------------------------------------
#  TASK 95 (Звездный прямоугольник)
#  -------------------------------------------------------------------------------------------------
#  На вход программе подается натуральное число n [1:20].
# Напишите программу, которая печатает звездный прямоугольник размерами n * 19
#  -------------------------------------------------------------------------------------------------

# num = int(input())
# for i in range(num):
#     print("*" * 19)

#  -------------------------------------------------------------------------------------------------
#  TASK 96 (Повторяй за мной 2)
#  -------------------------------------------------------------------------------------------------
#  Напишите программу, которая считывает одну строку текста и выводит 10 строк,
#  пронумерованных от 0 до 9, каждая с указанной строкой текста.
#  -------------------------------------------------------------------------------------------------

# text = input()
# for i in range(10):
#     print(i, text)

#  -------------------------------------------------------------------------------------------------
#  TASK 97 (Квадрат числа)
#  -------------------------------------------------------------------------------------------------
#  На вход программе подается натуральное число n. Напишите программу,
#  которая для каждого из чисел от 0 до n (включительно) выводит фразу:
#  «Квадрат числа [число] равен [число]» (без кавычек).
#  -------------------------------------------------------------------------------------------------

# num = int(input())
# for i in range(num + 1):
#     print("Квадрат числа", i, "равен", i ** 2)

#  -------------------------------------------------------------------------------------------------
#  TASK 98 (Звездный треугольник)
#  -------------------------------------------------------------------------------------------------
#  На вход программе подается натуральное число n, (n≥2) – катет прямоугольного равнобедренного треугольника.
#  Напишите программу, которая выводит звездный треугольник в соответствии с примером.
#  -------------------------------------------------------------------------------------------------

# num = int(input())
# for i in range(num):
#     print("*" * (num - i))

#  -------------------------------------------------------------------------------------------------
#  TASK 99 (Популяция)
#  -------------------------------------------------------------------------------------------------
#  На вход программе подается три натуральных числа m,p,n:
#  m: стартовое количество организмов; p: среднесуточное увеличение в %; n: количество дней для размножения.
#  Напишите программу, которая предсказывает размер популяции организмов.
#  Программа должна выводить размер популяции в каждый день, начиная с 11 и заканчивая nn-м днем.
#  -------------------------------------------------------------------------------------------------

# m, p, n = int(input()), int(input()), int(input())
# for i in range(n):
#     print(i + 1, float(m))
#     m = m * (1 + (p / 100))

#  -------------------------------------------------------------------------------------------------
#  TASK 100 (Последовательность чисел 1)
#  -------------------------------------------------------------------------------------------------
#  Даны два целых числа m <= n. Напишите программу, которая выводит все числа от m до n включительно.
#  -------------------------------------------------------------------------------------------------

# m, n = int(input()), int(input())
# for i in range(m, n+1):
#     print(i)

#  -------------------------------------------------------------------------------------------------
#  TASK 101 (Последовательность чисел 2)
#  -------------------------------------------------------------------------------------------------
#  Даны два целых числа m и n. Напишите программу, которая выводит все числа от m до n включительно
#  в порядке возрастания, если m < n, или в порядке убывания в противном случае.
#  -------------------------------------------------------------------------------------------------

# m, n = int(input()), int(input())
# if m == n:
#     print(m)
# elif m < n:
#     for i in range(m, n + 1):
#         print(i)
# else:
#     for i in range(m, n - 1, -1):
#         print(i)

#  -------------------------------------------------------------------------------------------------
#  TASK 102 (Последовательность чисел 3)
#  -------------------------------------------------------------------------------------------------
#  Даны два целых числа m > n. Напишите программу,
#  которая выводит все нечетные числа от m до n включительно в порядке убывания.
#  -------------------------------------------------------------------------------------------------

# m, n = int(input()), int(input())
# for i in range(m, n - 1, -1):
#     if i % 2 != 0:
#         print(i)

#  -------------------------------------------------------------------------------------------------
#  TASK 103 (Последовательность чисел 4)
#  -------------------------------------------------------------------------------------------------
#  Даны два натуральных числа m и n ( m≤n).
#  Напишите программу, которая выводит все числа от m до n включительно удовлетворяющие хотя бы одному из условий:
# число кратно 17;
# число оканчивается на 9;
# число кратно 3 и 5 одновременно.
#  -------------------------------------------------------------------------------------------------

# m, n = int(input()), int(input())
# for i in range(m, n + 1):
#     if i % 17 == 0 or i % 10 == 9 or (i % 3 == 0 and i % 5 == 0):
#         print(i)

#  -------------------------------------------------------------------------------------------------
#  TASK 104 (Таблица умножения)
#  -------------------------------------------------------------------------------------------------
#  Дано натуральное число n. Напишите программу, которая выводит таблицу умножения на n.
#  -------------------------------------------------------------------------------------------------

# num = int(input())
# for i in range(1, 11):
#     print(num, "x", i, "=", num * i)

#  -------------------------------------------------------------------------------------------------
#  TASK 105 (Количество чисел)
#  -------------------------------------------------------------------------------------------------
#  На вход программе подаются два целых числа a и b (a≤b). Напишите программу,
#  которая подсчитывает количество чисел в диапазоне от a до b включительно, куб которых оканчивается на 4 или 9.
#  -------------------------------------------------------------------------------------------------

# a, b, counter = int(input()), int(input()), 0
# for i in range(a, b + 1):
#     if i ** 3 % 10 == 4 or i ** 3 % 10 == 9:
#         counter += 1
# print(counter)

#  -------------------------------------------------------------------------------------------------
#  TASK 106 (Сумма чисел)
#  -------------------------------------------------------------------------------------------------
#  На вход программе подается натуральное число n, а затем n целых чисел, каждое на отдельной строке.
#  Напишите программу, которая подсчитывает сумму введенных чисел.
#  -------------------------------------------------------------------------------------------------

# n, total = int(input()), 0
# for i in range(n):
#     total += int(input())
# print(total)

#  -------------------------------------------------------------------------------------------------
#  TASK 107 (Асимптотическое приближение)
#  -------------------------------------------------------------------------------------------------
#  На вход программе подается натуральное число n. Напишите программу, которая вычисляет значение выражения
#  -------------------------------------------------------------------------------------------------

# import math
# n, temp = int(input()), 1
# for i in range(2, n + 1):
#     temp += (1 / i)
# print(temp - math.log(n))

#  -------------------------------------------------------------------------------------------------
#  TASK 108 (Сумма чисел 2)
#  -------------------------------------------------------------------------------------------------
#  На вход программе подается натуральное число n. Напишите программу,
#  которая подсчитывает сумму тех чисел от 1 до n (включительно) квадрат которых оканчивается на 2,5 или 8.
#  -------------------------------------------------------------------------------------------------

# n, total = int(input()), 0
# for i in range(1, n + 1):
#     if i ** 2 % 10 == 2 or i ** 2 % 10 == 5 or i ** 2 % 10 == 8:
#         total += i
# print(total)

#  -------------------------------------------------------------------------------------------------
#  TASK 109 (Факториал)
#  -------------------------------------------------------------------------------------------------
#  На вход программе подается натуральное число n. Напишите программу, которая вычисляет n!.
#  -------------------------------------------------------------------------------------------------

# n, f = int(input()), 1
# for i in range(2, n + 1):
#     f *= i
# print(f)

#  -------------------------------------------------------------------------------------------------
#  TASK 110 (Без нулей)
#  -------------------------------------------------------------------------------------------------
#  Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел.
#  -------------------------------------------------------------------------------------------------

# n = int(input())
# if n != 0:
#     temp = n
# else:
#     temp = 1
# for i in range(2, 11):
#     n = int(input())
#     if n != 0:
#         temp *= n
# print(temp)

#  -------------------------------------------------------------------------------------------------
#  TASK 111 (Без нулей)
#  -------------------------------------------------------------------------------------------------
#  Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел.
#  -------------------------------------------------------------------------------------------------

# n = int(input())
# if n != 0:
#     temp = n
# else:
#     temp = 1
# for i in range(2, 11):
#     n = int(input())
#     if n != 0:
#         temp *= n
# print(temp)

#  -------------------------------------------------------------------------------------------------
#  TASK 112 (Сумма делителей)
#  -------------------------------------------------------------------------------------------------
#  На вход программе подается натуральное число n. Напишите программу, которая вычисляет сумму всех его делителей.
#  -------------------------------------------------------------------------------------------------

# n, total = int(input()), 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         total += i
# print(total)

#  -------------------------------------------------------------------------------------------------
#  TASK 113 (Знакочередующаяся сумма)
#  -------------------------------------------------------------------------------------------------
#  На вход программе подается натуральное число n. Напишите программу вычисления знакочередующей суммы
#  -------------------------------------------------------------------------------------------------

# n, total = int(input()), 0
# for i in range(1, n + 1):
#     if i % 2 != 0:
#         total += i
#     else:
#         total -= i
# print(total)

#  -------------------------------------------------------------------------------------------------
#  TASK 114 (Наибольшие числа)
#  -------------------------------------------------------------------------------------------------
#  На вход программе подается натуральное число n, а затем nn различных натуральных чисел, каждое на отдельной строке.
#  Напишите программу, которая выводит наибольшее и второе наибольшее число последовательности.
#  -------------------------------------------------------------------------------------------------

# n, counter1, counter2 = int(input()), 0, 0
# for i in range(1, n + 1):
#     n = int(input())
#     if counter1 < n:
#         counter2 = counter1
#         counter1 = n
#     elif counter2 < n:
#         counter2 = n
# print(counter1)
# print(counter2)

#  -------------------------------------------------------------------------------------------------
#  TASK 115 (Only even numbers)
#  -------------------------------------------------------------------------------------------------
#  Напишите программу, которая считывает последовательность из 10 целых чисел и
#  определяет является ли каждое из них четным или нет.
#  -------------------------------------------------------------------------------------------------

# flag = True
# for i in range(1, 11):
#     n = int(input())
#     if n % 2 != 0:
#         flag = False
# if flag == True:
#     print("YES")
# else:
#     print("NO")

#  -------------------------------------------------------------------------------------------------
#  TASK 116 (Последовательность Фибоначчи)
#  -------------------------------------------------------------------------------------------------
#  Напишите программу, которая считывает натуральное число n и выводит первые n чисел последовательности Фибоначчи.
#  -------------------------------------------------------------------------------------------------

# n, num1, num2 = int(input()), 0, 1
# for i in range(n):
#     print(num2, "", end = '')
#     num1, num2 = num2, num1 + num2
