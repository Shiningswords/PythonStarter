# ---------------------------------------------------------------------------------------------
# ОБЪЯВЛЕНИЕ ФУНКЦИИ
# ---------------------------------------------------------------------------------------------
#  def hello_world():  # Объявление функции hello_world
#     print('Hello, World!')
#
#
# hello_world()   # Вызов функции hello_world
# ---------------------------------------------------------------------------------------------
# ФУНКЦИЯ С ПАРАМЕТРОМ
# ---------------------------------------------------------------------------------------------
# def print_numbers(limit):   # limit - формальный параметр функции print_numbers
#     for i in range(limit):
#         print(i)
#
#
# # Здесь вызывается функция print_numbers, а её формальный
# # параметр limit замещается фактическим параметром 10
# print_numbers(10)
# # Читаем ввод пользователя при помощи стандартной
# # функции input, конструируем из него число при
# # помощи стандартной функции int и записываем в
# # переменную n
# n = int(input('Введите n: '))
# # Вызываем функцию print_numbers с фактическим параметром n
# print_numbers(n)
# ---------------------------------------------------------------------------------------------
# ИСПОЛЬЗОВАНИЕ ФУНКЦИИ В ДРУГОЙ ФУНКЦИИ
# ---------------------------------------------------------------------------------------------
# Функция из прошлого примера
# def print_numbers(limit):
#     for i in range(limit):
#         print(i)
#
#
# # Любое логически завершённое действие следует помещать в функцию
# def main():
#     n = int(input('Введите n: '))
#     print_numbers(n)
#
#
# # Главную функцию желательно вызывать так
# # (таким образом функция будет вызвана только если
# # данный файл был запущен как главный; это важно
# # для приложений, состоящих из нескольких модулей)
# if __name__ == '__main__':
#     main()
# ---------------------------------------------------------------------------------------------
# ФУНКЦИЯ С ВОЗВРАТОМ ЗНАЧЕНИЯ
# ---------------------------------------------------------------------------------------------
# def add_numbers(a, b):
#     return a + b  # возврат суммы параметров
#
#
# x = add_numbers(2, 3)
# print(x)
# ---------------------------------------------------------------------------------------------
# def procedure():
#     print('I return nothing... Or I do?')
#
# value = procedure()
# print('Результат функции:', value) # Если не определить возвращаемое значение, то резултатом будет None
# ---------------------------------------------------------------------------------------------
# ФУНКЦИЯ С ПРЕДОПРЕДЕЛЕННЫМИ АРГУМЕНТАМИ
# ---------------------------------------------------------------------------------------------
# Если параметр name не задан, то name = 'Alex'
# def hello(name='Alex'):
#     print('Hello, ', name, '!', sep='')
#
# hello('Python')
# hello()
