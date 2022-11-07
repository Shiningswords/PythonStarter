#  -------------------------------------------------------------------------------------------------
#  TASK 220 (Звездный прямоугольник 1)
#  -------------------------------------------------------------------------------------------------
#   Напишите функцию draw_box(), которая выводит звездный прямоугольник с размерами 14×10 в соответствии с образцом:
#  -------------------------------------------------------------------------------------------------

# def draw_box():
#     print("*" * 10)
#     for _ in range(12):
#         print("*" + " " * 8 + "*")
#     print("*" * 10)

#  -------------------------------------------------------------------------------------------------
#  TASK 221 (Звездный треугольник 1)
#  -------------------------------------------------------------------------------------------------
#   Напишите функцию draw_triangle(), которая выводит звездный прямоугольный треугольник с катетами, равными 10
#  -------------------------------------------------------------------------------------------------

# def draw_triangle():
#     for i in range(1, 11):
#         print("*" * i)

#  -------------------------------------------------------------------------------------------------
#  TASK 222 (Звездный треугольник)
#  -------------------------------------------------------------------------------------------------
#   Напишите функцию draw_triangle(fill, base), которая принимает два параметра:
#   fill – символ заполнитель;
#   base – величина основания равнобедренного треугольника;
#   а затем выводит его.
#  -------------------------------------------------------------------------------------------------

# def draw_triangle(fill, base):
#     for i in range(1, base // 2 + 1):
#         print(fill * i)
#     for i in range(base // 2 + 1, 0, -1):
#         print(fill * i)

#  -------------------------------------------------------------------------------------------------
#  TASK 223 (ФИО)
#  -------------------------------------------------------------------------------------------------
#   Напишите функцию print_fio(name, surname, patronymic), которая принимает три параметра:
#   name – имя человека; surname – фамилия человека; patronymic – отчество человека;
#   а затем выводит на печать ФИО человека.
#  -------------------------------------------------------------------------------------------------

# def print_fio(name, surname, patronymic):
#     print(surname[0].upper() + name[0].upper() + patronymic[0].upper())

#  -------------------------------------------------------------------------------------------------
#  TASK 224 (Сумма цифр)
#  -------------------------------------------------------------------------------------------------
#   Напишите функцию print_digit_sum(), которая принимает одно целое число num и выводит на печать сумму его цифр.
#  -------------------------------------------------------------------------------------------------

# def print_digit_sum(num):
#     total = 0
#     while num > 0:
#         total += num % 10
#         num //= 10
#     print(total)
