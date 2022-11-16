#  -------------------------------------------------------------------------------------------------
#  TASK 034 (Таблица умножения)
#  -------------------------------------------------------------------------------------------------
#  На вход программе подаются два натуральных числа n и m — количество строк и столбцов в матрице.
#  Создайте матрицу mult размером n×m и заполните её таблицей умножения по формуле mult[i][j] = i * j.
#  -------------------------------------------------------------------------------------------------

# row, col, res = int(input()), int(input()), []
# for i in range(row):
#     res.append([0] * col)
# for i in range(row):
#     for j in range(col):
#         print(str(i*j).ljust(3), end='')
#     print()

#  -------------------------------------------------------------------------------------------------
#  TASK 035 (Максимум в таблице)
#  -------------------------------------------------------------------------------------------------
#  На вход программе подаются два натуральных числа n и m — количество строк и столбцов в матрице,
#  затем n строк по m целых чисел в каждой, отделенных символом пробела.
#  Напишите программу, которая находит индексы (строку и столбец) первого вхождения максимального элемента.
#  -------------------------------------------------------------------------------------------------

# row, col, res, a, b = int(input()), int(input()), [], 0, 0
# for i in range(row):
#     res.append([int(i) for i in input().split()])
# mx = res[0][0]
# for i in range(row):
#     for j in range(col):
#         if res[i][j] > mx:
#             mx = res[i][j]
#             a = i
#             b =j
# print(a, b)

#  -------------------------------------------------------------------------------------------------
#  TASK 036 (Обмен столбцов)
#  -------------------------------------------------------------------------------------------------
#  Напишите программу, которая меняет местами столбцы в матрице.
#  -------------------------------------------------------------------------------------------------

# row, col, res = int(input()), int(input()), []
# for i in range(row):
#     res.append([int(i) for i in input().split()])
# arr = [int(i) for i in input().split()]
# for k in range(row):
#     res[k][arr[0]], res[k][arr[1]] = res[k][arr[1]], res[k][arr[0]]
# for k in range(row):
#     for l in range(col):
#         print(res[k][l], end=' ')
#     print()

#  -------------------------------------------------------------------------------------------------
#  TASK 037 (Симметричная матрица)
#  -------------------------------------------------------------------------------------------------
#  Напишите программу, которая проверяет симметричность квадратной матрицы относительно главной диагонали.
#  -------------------------------------------------------------------------------------------------

# row, res, flag = int(input()), [], True
# for i in range(row):
#     res.append([0] * row)
# for i in range(row):
#     res[i] = [int(i) for i in input().split()]
# for i in range(row):
#     for j in range(row):
#         if res[i][j] != res[j][i]:
#             flag = False
# if flag:
#     print("YES")
# else:
#     print("NO")

#  -------------------------------------------------------------------------------------------------
#  TASK 038 (Обмен диагоналей)
#  -------------------------------------------------------------------------------------------------
#  Дана квадратная матрица чисел. Напишите программу, которая меняет местами элементы,
#  стоящие на главной и побочной диагонали, при этом каждый элемент должен остаться в том же столбце
#  (то есть в каждом столбце нужно поменять местами элемент на главной диагонали и на побочной диагонали).
#  -------------------------------------------------------------------------------------------------

# row, res = int(input()), []
# j = row - 1
# for i in range(row):
#     res.append([0] * row)
# for i in range(row):
#     res[i] = [int(i) for i in input().split()]
# for i in range(row):
#     res[row - i - 1][i], res[i][i] = res[i][i], res[row - i - 1][i]
# for i in range(row):
#     print(*res[i])

#  -------------------------------------------------------------------------------------------------
#  TASK 039 (Зеркальное отображение)
#  -------------------------------------------------------------------------------------------------
#  Дана квадратная матрица чисел. Напишите программу, которая зеркально отображает её элементы относительно
#  горизонтальной оси симметрии.
#  -------------------------------------------------------------------------------------------------

# row, res = int(input()), []
# for i in range(row):
#     res.append([0] * row)
# for i in range(row):
#     res.append([int(i) for i in input().split()])
# res.reverse()
# for i in range(row):
#     print(*res[i])

#  -------------------------------------------------------------------------------------------------
#  TASK 040 (Поворот матрицы)
#  -------------------------------------------------------------------------------------------------
#  Напишите программу, которая поворачивает квадратную матрицу чисел на 90∘ по часовой стрелке.
#  -------------------------------------------------------------------------------------------------

# row, res = int(input()), []
# for i in range(row):
#     res.append([0] * row)
# for i in range(row):
#     res[i] = [int(i) for i in input().split()]
# for i in range(row):
#     for j in range(row-1, -1, -1):
#         print(res[j][i], end=' ')
#     print()

#  -------------------------------------------------------------------------------------------------
#  TASK 041 (Ходы коня)
#  -------------------------------------------------------------------------------------------------
#  На шахматной доске 8×8 стоит конь. Напишите программу, которая отмечает положение коня на доске и все клетки,
#  которые бьет конь. Клетку, где стоит конь, отметьте английской буквой N, клетки, которые бьет конь,
#  отметьте символами *, остальные клетки заполните точками.
#  -------------------------------------------------------------------------------------------------

# inp = input()
# y = int('abcdefgh'.index(inp[0]))
# x = int(inp[1]) - 1
# for i in range(7, -1, -1):
#     for j in range(8):
#         if i == x and j == y:
#             print('N', end=' ')
#         elif (j == y - 2 and (x == i - 1 or x == i + 1)):
#             print('*', end=' ')
#         elif (j == y - 1 and (x == i - 2 or x == i + 2)):
#             print('*', end=' ')
#         elif (j == y + 2 and (x == i - 1 or x == i + 1)):
#             print('*', end=' ')
#         elif (j == y + 1 and (x == i - 2 or x == i + 2)):
#             print('*', end=' ')
#         else:
#             print('.', end=" ")
#     print()

#  -------------------------------------------------------------------------------------------------
#  TASK 042 (Магический квадрат)
#  -------------------------------------------------------------------------------------------------
#  Магическим квадратом порядка nn называется квадратная таблица размера n×n, составленная из всех чисел 1,2,3,…,n^2
#  так, что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между собой.
#  Напишите программу, которая проверяет, является ли заданная квадратная матрица магическим квадратом.
#  -------------------------------------------------------------------------------------------------

# n, arr, flag = int(input()), [], True
# for i in range(n):
#     arr.append([int(i) for i in input().split()])
# check, nums = 0, []
# for i in range(n):
#     check += arr[0][i]
# for i in range(n):
#     col, row = 0, 0
#     for j in range(n):
#         col += arr[j][i]
#         row += arr[i][j]
#         nums.append(arr[i][j])
#     if col != check or row != check:
#         flag = False
# d1, d2 = 0, 0
# for i in range(n):
#     d1 += arr[i][i]
#     d2 += arr[i][n-i-1]
# if d1 != check or d2 != check:
#     flag = False
# for i in range(1,n**2 + 1):
#     if i not in nums:
#         flag = False
# if flag:
#     print("YES")
# else:
#     print("NO")
