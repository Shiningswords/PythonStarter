#  -------------------------------------------------------------------------------------------------
#  TASK 053 (Сложение матриц)
#  -------------------------------------------------------------------------------------------------
#  Напишите программу для вычисления суммы двух матриц. На вход программе подаются два натуральных числа n и m —
#  количество строк и столбцов в матрицах, затем элементы первой матрицы, затем пустая строка,
#  далее следуют элементы второй матрицы.
#  -------------------------------------------------------------------------------------------------

# n, m = [int(i) for i in input().split()]
# m1, m2, res = [], [], []
# for _ in range(n):
#     m1.append([int(i) for i in input().split()])
# temp = input()
# for _ in range(n):
#     m2.append([int(i) for i in input().split()])
# for i in range(n):
#     res.append([])
#     for j in range(m):
#         res[i].append(m1[i][j] + m2[i][j])
# for i in range(n):
#     for j in range(m):
#         print(str(res[i][j]).ljust(3), end=" ")
#     print()

#  -------------------------------------------------------------------------------------------------
#  TASK 054 (Умножение матриц)
#  -------------------------------------------------------------------------------------------------
#  Напишите программу, которая перемножает две матрицы. На вход программе подаются два натуральных числа n и m —
#  количество строк и столбцов в первой матрице, затем элементы первой матрицы, затем пустая строка.
#  Далее следуют числа m и k — количество строк и столбцов второй матрицы затем элементы второй матрицы.
#  -------------------------------------------------------------------------------------------------

# n, m = [int(i) for i in input().split()]
# m1, m2, res = [], [], []
# for _ in range(n):
#     m1.append([int(i) for i in input().split()])
# temp = input()
# m, k = [int(i) for i in input().split()]
# for _ in range(m):
#     m2.append([int(i) for i in input().split()])
# for i in range(n):
#     res.append([])
#     for j in range(k):
#         temp = 0
#         for v in range(m):
#             temp += m1[i][v] * m2[v][j]
#         res[i].append(temp)
# for i in range(n):
#     for j in range(k):
#         print(str(res[i][j]).ljust(3), end=" ")
#     print()

#  -------------------------------------------------------------------------------------------------
#  TASK 055 (Возведение матрицы в степень)
#  -------------------------------------------------------------------------------------------------
#  Напишите программу, которая возводит квадратную матрицу в m-ую степень. На вход программе подаётся
#  натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы, затем натуральное число m.
#  -------------------------------------------------------------------------------------------------

# import copy
#
# n = int(input())
# mtrx, res = [], []
# for _ in range(n):
#     mtrx.append([int(i) for i in input().split()])
# res = copy.deepcopy(mtrx)
# mtrx2 = copy.deepcopy(res)
# m = int(input())
# for _ in range(m - 1):
#     for i in range(n):
#         for j in range(n):
#             temp = 0
#             for v in range(n):
#                 temp += res[i][v] * mtrx[v][j]
#             mtrx2[i][j] = temp
#         res = copy.deepcopy(mtrx2)
# for i in range(n):
#         for j in range(n):
#             print(str(res[i][j]).ljust(3), end=" ")
#         print()