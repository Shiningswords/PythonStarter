#  -------------------------------------------------------------------------------------------------
#  TASK 176 (Каждый третий)
#  -------------------------------------------------------------------------------------------------
#   На вход программе подается строка текста. Напишите программу,
#   которая удаляет из нее все символы с индексами кратными 3 (0, 3, 6, 9....)
#  -------------------------------------------------------------------------------------------------

# text, res = input(), ''
# for i in range(len(text)):
#     if i % 3 != 0:
#         res += text[i]
# print(res)

#  -------------------------------------------------------------------------------------------------
#  TASK 177 (Замени меня полностью)
#  -------------------------------------------------------------------------------------------------
#   На вход программе подается строка текста. Напишите программу, которая заменяет все вхождения цифры 1 на слово «one».
#  -------------------------------------------------------------------------------------------------

# text = input()
# print(text.replace('1', 'one'))

#  -------------------------------------------------------------------------------------------------
#  TASK 178 (Удали меня полностью)
#  -------------------------------------------------------------------------------------------------
#   На вход программе подается строка текста. Напишите программу, которая удаляет все вхождения символа «@».
#  -------------------------------------------------------------------------------------------------

# text = input()
# print(text.replace('@', ''))

#  -------------------------------------------------------------------------------------------------
#  TASK 179 (Второе вхождение)
#  -------------------------------------------------------------------------------------------------
#   На вход программе подается строка текста. Напишите программу, которая выводит индекс второго вхождения буквы «f».
#   Если буква «f» встречается только один раз, выведите число -1, а если не встречается ни разу, выведите число -2.
#  -------------------------------------------------------------------------------------------------

# text = input()
# counter = text.count('f')
# if counter == 0:
#     print(-2)
# elif counter == 1:
#     print(-1)
# else:
#     print(text.find('f', text.find('f') + 1))

#  -------------------------------------------------------------------------------------------------
#  TASK 180 (Переворот)
#  -------------------------------------------------------------------------------------------------
#   На вход программе подается строка текста в которой буква «h» встречается как минимум два раза.
#   Напишите программу, которая возвращает исходную строку и переворачивает последовательность символов,
#   заключенную между первым и последним вхождением буквы «h».
#  -------------------------------------------------------------------------------------------------

# text, res = input(), ''
# res += text[:text.find('h')]
# for i in range( text.rfind('h'), text.find('h'), -1):
#     res += text[i]
# res += text[text.rfind('h'):]
# print(res)
