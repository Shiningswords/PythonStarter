#  -------------------------------------------------------------------------------------------------
#  TASK 58 (Начало столетия)
#  -------------------------------------------------------------------------------------------------
#  Напишите программу, которая определяет, оканчивается ли год с данным номером на два нуля.
#  Если год оканчивается, то выведите «YES», иначе выведите «NO».
#  -------------------------------------------------------------------------------------------------

# year = int(input())
# if year % 10 == 0 and year % 100 // 10 == 0:
#     print("YES")
# else:
#     print("NO")

#  -------------------------------------------------------------------------------------------------
#  TASK 59 (Шахматная доска)
#  -------------------------------------------------------------------------------------------------
#  Заданы две клетки шахматной доски. Напишите программу, которая определяет имеют ли клетки один цвет или нет.
#  Если они покрашены в один цвет, то выведите слово «YES», а если в разные цвета — то «NO».
#  -------------------------------------------------------------------------------------------------

# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# if (x1 + y1 + x2 + y2) % 2 == 0:
#     print("YES")
# else:
#     print("NO")

#  -------------------------------------------------------------------------------------------------
#  TASK 60 (Girls only)
#  -------------------------------------------------------------------------------------------------
#  Футбольная команда набирает девочек от 10 до 15 лет включительно. Напишите программу,
#  которая запрашивает возраст и пол претендента, используя обозначение пола буквы m (от male – мужчина) и
#  f (от female – женщина) и определяет подходит ли претендент для вступления в команду или нет.
#  Если претендент подходит, то выведите «YES», иначе выведите «NO».
#  -------------------------------------------------------------------------------------------------

age, sex = int(input()), input()
if sex == 'f' and (10 <= age <= 15):
    print("YES")
else:
    print("NO")

#  -------------------------------------------------------------------------------------------------
#  TASK 61 (Римские цифры)
#  -------------------------------------------------------------------------------------------------
#  Напишите программу, которая считывает целое число и выводит соответствующую ему римскую цифру.
#  Если число находится вне диапазона 1-10, то программа должна вывести текст «ошибка».
#  -------------------------------------------------------------------------------------------------

# num = int(input())
# if num == 1:
#     print("I")
# elif num == 2:
#     print("II")
# elif num == 3:
#     print("III")
# elif num == 4:
#     print("IV")
# elif num == 5:
#     print("V")
# elif num == 6:
#     print("VI")
# elif num == 7:
#     print("VII")
# elif num == 8:
#     print("VIII")
# elif num == 9:
#     print("IX")
# elif num == 10:
#     print("X")
# else:
#     print("ошибка")

#  -------------------------------------------------------------------------------------------------
#  TASK 62 (YES or NO вот в чем вопрос)
#  -------------------------------------------------------------------------------------------------
#  Напишите программу, которая принимает на вход число и в зависимости от условий выводит текст «YES», либо «NO».
# Условия:
# если число нечётное, то вывести «YES»;
# если число чётное в диапазоне от 2 до 5 (включительно), то вывести «NO»;
# если число чётное в диапазоне от 6 до 20 (включительно), то вывести «YES»;
# если число чётное и больше 20, то вывести «NO».
#  -------------------------------------------------------------------------------------------------

# num = int(input())
# if num % 2 != 0 or (num % 2 == 0 and (6 <= num <= 20)):
#     print("YES")
# elif num % 2 == 0 or (num % 2 != 0 and (2 <= num <= 5)):
#     print("NO")

#  -------------------------------------------------------------------------------------------------
#  TASK 63 (Ход слона)
#  -------------------------------------------------------------------------------------------------
#  Даны две различные клетки шахматной доски. Напишите программу, которая определяет,
#  может ли слон попасть с первой клетки на вторую одним ходом.
#  Программа получает на вход четыре числа от 1 до 8 каждое,
#  задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.
#  Программа должна вывести YES, если из первой клетки ходом слона можно попасть во вторую или NO в противном случае.
#  -------------------------------------------------------------------------------------------------

# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# if x1 - y1 == x2 - y2 or x1 + y1 == x2 + y2:
#     print("YES")
# else:
#     print("NO")

#  -------------------------------------------------------------------------------------------------
#  TASK 64 (Ход коня)
#  -------------------------------------------------------------------------------------------------
#  Даны две различные клетки шахматной доски. Напишите программу,  которая определяет,
#  может ли конь попасть с первой клетки на вторую одним ходом.
#  Программа получает на вход четыре числа от 1 до 8 каждое,
#  задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.
#  Программа должна вывести «YES», если из первой клетки ходом коня можно попасть во вторую или «NO» в противном случае.
#  -------------------------------------------------------------------------------------------------

# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# if x1 - 2 == x2 and (y1 - 1 == y2 or y1 + 1 == y2):
#     print("YES")
# elif x1 - 1 == x2 and (y1 - 2 == y2 or y1 + 2 == y2):
#     print("YES")
# elif x1 + 1 == x2 and (y1 - 2 == y2 or y1 + 2 == y2):
#     print("YES")
# elif x1 + 2 == x2 and (y1 - 1 == y2 or y1 + 1 == y2):
#     print("YES")
# else:
#     print("NO")

#  -------------------------------------------------------------------------------------------------
#  TASK 65 (Ход ферзя)
#  -------------------------------------------------------------------------------------------------
#  Даны две различные клетки шахматной доски. Напишите программу,
#  которая определяет, может ли ферзь попасть с первой клетки на вторую одним ходом.
#  Программа получает на вход четыре числа от 1 до 8 каждое,
#  задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.
#  Программа должна вывести YES, если из первой клетки ходом ферзя можно попасть во вторую или NO в противном случае.
#  -------------------------------------------------------------------------------------------------

# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# if x2 == x1 or y2 == y1:
#     print("YES")
# elif x1 - y1 == x2 - y2 or x1 + y1 == x2 + y2:
#     print("YES")
# else:
#     print("NO")
