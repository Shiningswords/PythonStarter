#  -------------------------------------------------------------------------------------------------
#  TASK 78 (What's Your Name?)
#  -------------------------------------------------------------------------------------------------
#  Напишите программу, которая считывает с клавиатуры две строки – имя и фамилию пользователя и выводит фразу:
#  «Hello [введенное имя] [введенная фамилия]! You just delved into Python».
#  -------------------------------------------------------------------------------------------------

# str1, str2 = input(), input()
# print("Hello " + str1 + " " + str2 +"! You just delved into Python")

#  -------------------------------------------------------------------------------------------------
#  TASK 79 (Футбольная команда)
#  -------------------------------------------------------------------------------------------------
#  Напишите программу, которая считывает с клавиатуры название футбольной команды и выводит фразу:
# «Футбольная команда [введённая строка] имеет длину [длина введённой строки] символов».
#  -------------------------------------------------------------------------------------------------

# team = input()
# print("Футбольная команда " + team + " имеет длину " + str(len(team)) + " символов")

#  -------------------------------------------------------------------------------------------------
#  TASK 80 (Три города)
#  -------------------------------------------------------------------------------------------------
#  Даны названия трех городов. Напишите программу, которая определяет самое короткое и самое длинное название города.
#  -------------------------------------------------------------------------------------------------

# city1, city2, city3 = input(), input(), input()
# len1, len2, len3 = len(city1), len(city2), len(city3)
# if len1 == min(len1, len2, len3):
#     print(city1)
# elif len2 == min(len1, len2, len3):
#     print(city2)
# elif len3 == min(len1, len2, len3):
#     print(city3)
# if len1 == max(len1, len2, len3):
#     print(city1)
# elif len2 == max(len1, len2, len3):
#     print(city2)
# elif len3 == max(len1, len2, len3):
#     print(city3)

#  -------------------------------------------------------------------------------------------------
#  TASK 81 (Арифметические строки)
#  -------------------------------------------------------------------------------------------------
#  Вводятся 3 строки в случайном порядке. Напишите программу, которая выясняет можно ли из длин этих строк построить
#  возрастающую арифметическую прогрессию.
#  -------------------------------------------------------------------------------------------------

# len1, len2, len3 = len(input()), len(input()), len(input())
# maxLen, minLen, midLen = max(len1, len2, len3), min(len1, len2, len3), len1 + len2 + len3 - max(len1, len2, len3) - min(len1, len2, len3)
# if midLen - minLen == maxLen - midLen:
#     print("YES")
# else:
#     print("NO")

#  -------------------------------------------------------------------------------------------------
#  TASK 82 (Цвет настроения синий)
#  -------------------------------------------------------------------------------------------------
#  Напишите программу, которая считывает одну строку, после чего выводит «YES»,
#  если в введенной строке есть подстрока «синий» и «NO» в противном случае.
#  -------------------------------------------------------------------------------------------------

# text = input()
# if "синий" in text:
#     print("YES")
# else:
#     print("NO")

#  -------------------------------------------------------------------------------------------------
#  TASK 83 (Отдыхаем ли?)
#  -------------------------------------------------------------------------------------------------
#  Напишите программу, которая считывает одну строку, после чего выводит «YES»,
#  если в введённой строке есть подстрока «суббота» или «воскресенье», и «NO» в противном случае.
#  -------------------------------------------------------------------------------------------------

# text = input()
# if "суббота" in text or "воскресенье" in text:
#     print("YES")
# else:
#     print("NO")

#  -------------------------------------------------------------------------------------------------
#  TASK 84 (Корректный email)
#  -------------------------------------------------------------------------------------------------
#  Будем считать email адрес корректным, если в нем есть символ собачки (@) и точки.
#  Напишите программу проверяющую корректность email адреса.
#  -------------------------------------------------------------------------------------------------

# email = input()
# if "@" in email and "." in email:
#     print("YES")
# else:
#     print("NO")
