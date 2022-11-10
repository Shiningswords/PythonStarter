def encryption(lang, stp, txt):
    res = ''
    if lang == 'Русский':
        for c in txt:
            if c in RUS_LOW:
                if ord(c) + stp > 1103:
                    res += chr(((ord(c) + stp) - 1103) + 1071)
                else:
                    res += chr(ord(c) + stp)
            if c in RUS_UP:
                if ord(c) + stp > 1071:
                    res += chr(((ord(c) + stp) - 1071) + 1039)
                else:
                    res += chr(ord(c) + stp)
            if c not in RUS_LOW and c not in RUS_UP:
                res += c
        return res
    else:
        for c in txt:
            if c in ENG_LOW:
                if ord(c) + stp > 122:
                    res += chr(((ord(c) + stp) - 122) + 96)
                else:
                    res += chr(ord(c) + stp)
            if c in ENG_UP:
                if ord(c) + stp > 90:
                    res += chr(((ord(c) + stp) - 90) + 64)
                else:
                    res += chr(ord(c) + stp)
            if c not in ENG_LOW and c not in ENG_UP:
                res += c
    return res


RUS_LOW = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
RUS_UP = 'АБВГДЕЖЗИКЛМНОПРСТУФЦЧШЩЪЫЬЭЮЯ'
ENG_LOW = 'abcdefghijklmnopqrstuvwxyz'
ENG_UP = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('Добро пожаловать в программу "ШИФР ЦЕЗАРЯ')

while True:
    cipher = input('Введите "+" для шифрования и "-" для дешифрования: ')
    if cipher == '+' or cipher == '-':
        break
    else:
        print('Введите корректные данные')

while True:
    language = input('Введите "Русский" для использования русского языка и "Английский" для английского языка: ')
    if language == 'Русский' or language == 'Английский':
        break
    else:
        print('Введите корректные данные')

while True:
    try:
        step = int(input('Введите шаг шифрования: '))
        break
    except ValueError:
        print('Введите корректные данные')

text = input('Введите текст для шифрования/дешифрования: ')
print(encryption(language, step, text))
