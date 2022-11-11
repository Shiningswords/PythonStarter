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


def decryption(lang, stp, txt):
    res = ''
    if lang == 'Русский':
        for c in txt:
            if c in RUS_LOW:
                if ord(c) - stp < 1072:
                    res += chr(1104 + ((ord(c) - stp) - 1072))
                else:
                    res += chr(ord(c) - stp)
            if c in RUS_UP:
                if ord(c) - stp < 1040:
                    res += chr(1072 + ((ord(c) - stp) - 1040))
                else:
                    res += chr(ord(c) - stp)
            if c not in RUS_LOW and c not in RUS_UP:
                res += c
        return res
    else:
        for c in txt:
            if c in ENG_LOW:
                if ord(c) - stp < 97:
                    res += chr(123 + ((ord(c) - stp) - 97))
                else:
                    res += chr(ord(c) - stp)
            if c in ENG_UP:
                if ord(c) - stp < 65:
                    res += chr(91 + ((ord(c) - stp) - 65))
                else:
                    res += chr(ord(c) - stp)
            if c not in ENG_LOW and c not in ENG_UP:
                res += c
    return res


RUS_LOW = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
RUS_UP = 'АБВГДЕЖЗИКЛМНОПРСТУФЦЧШЩЪЫЬЭЮЯ'
ENG_LOW = 'abcdefghijklmnopqrstuvwxyz'
ENG_UP = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('Добро пожаловать в программу "ШИФР ЦЕЗАРЯ"')

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
        step = int(input(f'Введите шаг {"шифрования" if cipher == "+" else "дешифрования"}: '))
        if step < 0:
            print('Введите корректные данные')
        else:
            break
    except ValueError:
        print('Введите корректные данные')

text = input(f'Введите текст для {"шифрования" if cipher == "+" else "дешифрования"}: ')

if cipher == '+':
    print(encryption(language, step, text))
else:
    print(decryption(language, step, text))
