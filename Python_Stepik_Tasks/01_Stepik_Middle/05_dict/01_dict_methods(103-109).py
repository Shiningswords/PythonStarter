#  -------------------------------------------------------------------------------------------------
#  TASK 103 (Словарь программиста)
#  -------------------------------------------------------------------------------------------------
#  Программисты, как вы уже знаете, постоянно учатся, а в общении между собой используют весьма специфический язык.
#  Чтобы систематизировать ваш пополняющийся профессиональный лексикон, мы придумали эту задачу.
#  Напишите программу создания небольшого словаря сленговых программерских выражений,
#  чтобы она потом по запросу возвращала значения из этого словаря.
#  -------------------------------------------------------------------------------------------------

# n, dict1 = int(input()), {}
# for i in range(n):
#     temp = input().split(':')
#     temp[1] = temp[1].strip()
#     dict1[temp[0].lower()] = temp[1]
# m = int(input())
# for i in range(m):
#     word = input().lower()
#     if word in dict1.keys():
#         print(dict1[word])
#     else:
#         print("Не найдено")

#  -------------------------------------------------------------------------------------------------
#  TASK 104 (Анаграммы 1)
#  -------------------------------------------------------------------------------------------------
#  Анаграмма – слово (словосочетание), образованное путём перестановки букв, составляющих другое слово (словосочетание).
#  Например, английские слова evil и live – это анаграммы.
#  -------------------------------------------------------------------------------------------------

# print("YES" if sorted(input()) == sorted(input()) else "NO")

#  -------------------------------------------------------------------------------------------------
#  TASK 105 (Анаграммы 2)
#  -------------------------------------------------------------------------------------------------
#  На вход программе подаются два предложения. Напишите программу, которая определяет, являются они анаграммами или нет.
#  Ваша программа должна игнорировать регистр символов, знаки препинания и пробелы.
#  -------------------------------------------------------------------------------------------------

# txt1 = ''.join(i.lower() for i in input() if i.isalpha())
# txt2 = ''.join(i.lower() for i in input() if i.isalpha())
# print("YES" if sorted(txt1) == sorted(txt2) else "NO")

#  -------------------------------------------------------------------------------------------------
#  TASK 106 (Словарь синонимов)
#  -------------------------------------------------------------------------------------------------
#  Вам дан словарь, состоящий из пар слов-синонимов. Повторяющихся слов в словаре нет.
#  Напишите программу, которая для одного данного слова определяет его синоним.
#  -------------------------------------------------------------------------------------------------

# n, dict1, dict2 = int(input()), {}, {}
# for _ in range(n):
#     words = input().split()
#     dict1[words[0]] = words[1]
#     dict2[words[1]] = words[0]
# w = input()
# if w in dict1:
#     print(dict1[w])
# else:
#     print(dict2[w])

#  -------------------------------------------------------------------------------------------------
#  TASK 107 (Страны и города)
#  -------------------------------------------------------------------------------------------------
#  На вход программе подается список стран и городов каждой страны. Затем даны названия городов.
#  Напишите программу, которая для каждого города выводит, в какой стране он находится.
#  -------------------------------------------------------------------------------------------------

# n, dict1 = int(input()), {}
# for _ in range(n):
#     words = input().split()
#     for i in range(1, len(words)):
#         dict1[words[i]] = words[0]
# m = int(input())
# for _ in range(m):
#     print(dict1[input()])

#  -------------------------------------------------------------------------------------------------
#  TASK 108 (Телефонная книга)
#  -------------------------------------------------------------------------------------------------
#  Тимур записал телефоны всех своих друзей, чтобы автоматизировать поиск нужного номера.
#  У каждого из друзей Тимура может быть один или более телефонных номеров. Напишите программу,
#  которая поможет Тимуру находить все номера определённого друга.
#  -------------------------------------------------------------------------------------------------

# n, dict1 = int(input()), {}
# for _ in range(n):
#     temp = input().split()
#     dict1.setdefault(temp[1].lower(), []).append(temp[0])
# m = int(input())
# for _ in range(m):
#     req = input().lower()
#     if req in dict1:
#         print(*dict1[req])
#     else:
#         print('абонент не найден')

#  -------------------------------------------------------------------------------------------------
#  TASK 109 (Секретное слово)
#  -------------------------------------------------------------------------------------------------
#  Напишите программу для расшифровки секретного слова методом частотного анализа.
#  -------------------------------------------------------------------------------------------------

# word = input()
# n, dict1 = int(input()), {}
# for _ in range(n):
#     temp = input().split(":")
#     dict1[int(temp[1])] = temp[0]
# for c in word:
#     if word.count(c) in dict1:
#         print(dict1[word.count(c)], end='')
