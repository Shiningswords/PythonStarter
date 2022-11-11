#  -------------------------------------------------------------------------------------------------
#  TASK 001 (На easy)
#  -------------------------------------------------------------------------------------------------
#  На вход программе подаются два целых числа a и b. Напишите программу, которая выводит:
#  сумму чисел a и b; разность чисел a и b; произведение чисел a и b; частное чисел a и b;
#  целую часть от деления числа a на b; остаток от деления числа a на b; корень квадратный из суммы их 10-х степеней
#  -------------------------------------------------------------------------------------------------

# import math
# a, b = int(input()), int(input())
# print(a + b, a - b, a * b, a / b, a // b, a % b, math.sqrt(a ** 10 + b ** 10))

#  -------------------------------------------------------------------------------------------------
#  TASK 002 (Индекс массы тела)
#  -------------------------------------------------------------------------------------------------
#  Напишите программу для вычисления и оценки индекса массы тела (ИМТ) человека.
#  ИМТ показывает весит человек больше или меньше нормы для своего роста. ИМТ человека рассчитывают по формуле:
#  масса / (рост * рост)
#  -------------------------------------------------------------------------------------------------

# weight, height = float(input()), float(input())
# imt = weight / (height * height)
# if 18.5 <= imt <= 25:
#     print('Оптимальная масса')
# elif imt > 25:
#     print('Избыточная масса')
# else:
#     print('Недостаточная масса')

#  -------------------------------------------------------------------------------------------------
#  TASK 003 (Стоимость строки)
#  -------------------------------------------------------------------------------------------------
#  Дана строка текста. Напишите программу для подсчета стоимости строки, исходя из того, что один любой символ
#  (в том числе пробел) стоит 60 копеек. Ответ дайте в рублях и копейках в соответствии с примерами.
#  -------------------------------------------------------------------------------------------------

# text, total = input(), 0
# for i in range(len(text)):
#     total += 60
# print(total // 100, "р.", total % 100, "коп.")

#  -------------------------------------------------------------------------------------------------
#  TASK 004 (Количество слов)
#  -------------------------------------------------------------------------------------------------
#  Дана строка, состоящая из слов, разделенных пробелами. Напишите программу,
#  которая подсчитывает количество слов в этой строке.
#  -------------------------------------------------------------------------------------------------

# text = input()
# print(len(text.split()))

#  -------------------------------------------------------------------------------------------------
#  TASK 005 (Зодиак)
#  -------------------------------------------------------------------------------------------------
#  Китайский гороскоп назначает животным годы в 1212-летнем цикле. Один 1212-летний цикл показан в таблице ниже.
#  Таким образом, 20122012 год будет очередным годом дракона.
#  Год	Животное
#  2000	Дракон 2001	Змея 2002 Лошадь 2003 Овца 2004	Обезьяна 2005 Петух 2006 Собака 2007 Свинья 2008 Крыса 2009 Бык
#  2010	Тигр 2011 Заяц
#  Напишите программу, которая считывает год и отображает название связанного с ним животного.
#  Ваша программа должна корректно работать с любым годом, не только теми, что перечислены в таблице.
#  -------------------------------------------------------------------------------------------------

# arr = ["Дракон", "Змея", "Лошадь", "Овца", "Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц"]
# print(arr[(int(input()) + 4) % 12])

#  -------------------------------------------------------------------------------------------------
#  TASK 006 (Зодиак)
#  -------------------------------------------------------------------------------------------------
#  Дано пятизначное или шестизначное натуральное число. Напишите программу,
#  которая изменит порядок его последних пяти цифр на обратный.
#  -------------------------------------------------------------------------------------------------

# num = input()
# if len(num) == 5:
#     print(int(num[::-1]))
# else:
#     print(int(num[0] + num[:-6:-1]))

#  -------------------------------------------------------------------------------------------------
#  TASK 007 (Standard American Convention)
#  -------------------------------------------------------------------------------------------------
#  На вход программе подаётся натуральное число. Напишите программу, которая вставляет в заданное число запятые
#  в соответствии со стандартным американским соглашением о запятых в больших числах.
#  -------------------------------------------------------------------------------------------------

# num, res, counter = input(), "", 0
# for i in range(-1, -len(num)-1, -1):
#     if counter == 3:
#         res = "," + res
#         counter = 0
#     res = num[i] + res
#     counter += 1
# print(res)

#  -------------------------------------------------------------------------------------------------
#  TASK 008 (Задача Иосифа Флавия)
#  -------------------------------------------------------------------------------------------------
#  n человек, пронумерованных числами от 1 до n, стоят в кругу. Они начинают считаться, каждый k-й по счету человек
#  выбывает из круга, после чего счет продолжается со следующего за ним человека.
#  Напишите программу, определяющую номер человека, который останется в кругу последним.
#  -------------------------------------------------------------------------------------------------

# n, k = int(input()), int(input())
# arr = [int(i) for i in range(1, n+1)]
# counter, mx = 1, 0
# while len(arr) > 1:
#     if mx > len(arr) - 1:
#         mx = 0
#     if counter == k:
#         arr.pop(mx)
#         counter = 0
#         mx -= 1
#     counter += 1
#     mx += 1
# print(*arr)
