#  -------------------------------------------------------------------------------------------------
#  TASK 85 (Евклидово расстояние)
#  -------------------------------------------------------------------------------------------------
#  Напишите программу определяющую евклидово расстояние между двумя точками, координаты которых заданы.
#  -------------------------------------------------------------------------------------------------

# import math
# x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
# print(math.sqrt((x1-x2) ** 2 + (y1-y2) ** 2))

#  -------------------------------------------------------------------------------------------------
#  TASK 86 (Площадь и длина)
#  -------------------------------------------------------------------------------------------------
#  Напишите программу определяющую площадь круга и длину окружности по заданному радиусу
#  -------------------------------------------------------------------------------------------------

# import math
# R = float(input())
# print(math.pi * R ** 2)
# print(2 * math.pi * R)

#  -------------------------------------------------------------------------------------------------
#  TASK 87 (Средние значения)
#  -------------------------------------------------------------------------------------------------
#  В математике выделяют следующие средние значения: среднее арифметическое чисел,
#  среднее геометрическое чисел, среднее гармоническое чисел, среднее квадратичное чисел
#  -------------------------------------------------------------------------------------------------

# import math
# a, b = float(input()), float(input())
# print((a + b) / 2)
# print(math.sqrt(a * b))
# print((2 * a * b) / (a + b))
# print(math.sqrt((a ** 2 + b ** 2) / 2))

#  -------------------------------------------------------------------------------------------------
#  TASK 88 (Тригонометрическое выражение)
#  -------------------------------------------------------------------------------------------------
#  Напишите программу, вычисляющую значение тригонометрического выражения sin x + cos x + tan**2 x
#  -------------------------------------------------------------------------------------------------

# import math
# x = math.radians(float(input()))
# print(math.sin(x) + math.cos(x) + math.tan(x) ** 2)

#  -------------------------------------------------------------------------------------------------
#  TASK 89 (Пол и потолок)
#  -------------------------------------------------------------------------------------------------
#  Напишите программу, вычисляющую значение x + x (округ. к большему и меньшему) по заданному вещественному числу
#  -------------------------------------------------------------------------------------------------

# import math
# x = float(input())
# print(math.ceil(x) + math.floor(x))

#  -------------------------------------------------------------------------------------------------
#  TASK 90 (Квадратное уравнение)
#  -------------------------------------------------------------------------------------------------
#  Даны три вещественных числа Напишите программу, которая находит вещественные корни квадратного уравнения
#  -------------------------------------------------------------------------------------------------

# import math
# a, b, c = float(input()), float(input()), float(input())
# d = b ** 2 - 4 * a * c
# if d < 0:
#   print("Нет корней")
# elif  d == 0:
#   print(-(b / (2 * a)))
# else:
#   x1 = (-b - math.sqrt(d))/ (2 * a)
#   x2 = (-b + math.sqrt(d)) / (2 * a)
#   print(min(x1, x2))
#   print(max(x1, x2))

#  -------------------------------------------------------------------------------------------------
#  TASK 91 (Правильный многоугольник)
#  -------------------------------------------------------------------------------------------------
#  Правильный многоугольник — выпуклый многоугольник, у которого равны все стороны и все углы между смежными сторонами.
#  -------------------------------------------------------------------------------------------------

# import math
# n, a = int(input()), float(input())
# print((n * a ** 2) / (4 * math.tan(math.pi / n)))
