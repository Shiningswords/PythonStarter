#  -------------------------------------------------------------------------------------------------
#  TASK 41 (Принадлежность 1)
#  -------------------------------------------------------------------------------------------------
#  Напишите программу, которая принимает целое число x и определяет,
#  принадлежит ли данное число указанному промежутку. (-1:17)
#  -------------------------------------------------------------------------------------------------

# num = int(input())
# if -1 < num < 17:
#     print("Принадлежит")
# else:
#     print("Не принадлежит")

#  -------------------------------------------------------------------------------------------------
#  TASK 42 (Принадлежность 2)
#  -------------------------------------------------------------------------------------------------
#  Напишите программу, которая принимает целое число x и определяет,
#  принадлежит ли данное число указанным промежуткам.   [:-3][7:]
#  -------------------------------------------------------------------------------------------------

# num = int(input())
# if num <= -3 or num >= 7:
#     print("Принадлежит")
# else:
#     print("Не принадлежит")

#  -------------------------------------------------------------------------------------------------
#  TASK 43 (Принадлежность 3)
#  -------------------------------------------------------------------------------------------------
#  Напишите программу, которая принимает целое число x и определяет,
#  принадлежит ли данное число указанным промежуткам.   [-30:-2][7:25]
#  -------------------------------------------------------------------------------------------------

# num = int(input())
# if -30 < num <= -2 or 7 < num <= 25:
#     print("Принадлежит")
# else:
#     print("Не принадлежит")

#  -------------------------------------------------------------------------------------------------
#  TASK 44 (Красивое число)
#  -------------------------------------------------------------------------------------------------
#  Назовем число красивым, если оно является четырехзначным и делится нацело на 7 или на 17.
#  Напишите программу, определяющую, является ли введённое число красивым.
#  Программа должна вывести «YES», если число является красивым, или «NO» в противном случае.
#  -------------------------------------------------------------------------------------------------

# num = int(input())
# if 1000 <= num <= 9999 and (num % 7 == 0 or num % 17 == 0):
#     print("YES")
# else:
#     print("NO")

#  -------------------------------------------------------------------------------------------------
#  TASK 45 (Неравенство треугольника)
#  -------------------------------------------------------------------------------------------------
#  Напишите программу, которая принимает три положительных числа и определяет,
#  существует ли невырожденный треугольник с такими сторонами.
#  -------------------------------------------------------------------------------------------------

# a, b, c = int(input()), int(input()), int(input())
# if c < a + b and a < c + b and b < a + c:
#   print("YES")
# else:
#   print("NO")

#  -------------------------------------------------------------------------------------------------
#  TASK 46 (Високосный год)
#  -------------------------------------------------------------------------------------------------
#  Напишите программу, которая определяет, является ли год с данным номером високосным.
#  Если год является високосным, то выведите «YES», иначе выведите «NO».
#  Год является високосным, если его номер кратен 4, но не кратен 100, или если он кратен 400.
#  -------------------------------------------------------------------------------------------------

# year = int(input())
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#  print("YES")
# else:
#  print("NO")

#  -------------------------------------------------------------------------------------------------
#  TASK 47 (Ход ладьи)
#  -------------------------------------------------------------------------------------------------
#  Даны две различные клетки шахматной доски. Напишите программу, которая определяет,
#  может ли ладья попасть с первой клетки на вторую одним ходом.
#  Программа получает на вход четыре числа от 1 до 8 каждое,
#  задающие номер столбца и номер строки сначала для первой клетки,
#  потом для второй клетки. Программа должна вывести «YES»,
#  если из первой клетки ходом ладьи можно попасть во вторую, или «NO» в противном случае.
#  -------------------------------------------------------------------------------------------------

# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# if x1 == x2 or y1 == y2:
#   print("YES")
# else:
#   print("NO")

#  -------------------------------------------------------------------------------------------------
#  TASK 48 (Ход короля)
#  -------------------------------------------------------------------------------------------------
#  Напишите программу, которая определяет, является ли год с данным номером високосным.
#  Если год является високосным, то выведите «YES», иначе выведите «NO».
#  Год является високосным, если его номер кратен 4, но не кратен 100, или если он кратен 400.
#  -------------------------------------------------------------------------------------------------

# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# if (x1 - 1 <= x2 <= x1 + 1) and (y1 - 1 <= y2 <= y1 + 1):
#   print("YES")
# else:
#   print("NO")
