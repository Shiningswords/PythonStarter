import random


def assembly(digits_on, up_on, low_on, punctuation_on, except_on, res):
    if digits_on == 'Y':
        res += DIGITS
    if up_on == 'Y':
        res += UP_LETTERS
    if low_on == 'Y':
        res += LOW_LETTERS
    if punctuation_on == 'Y':
        res += PUNCTUATION
    if except_on == 'Y':
        res = res.replace('i', '')
        res = res.replace('I', '')
        res = res.replace('L', '')
        res = res.replace('l', '')
        res = res.replace('0', '')
        res = res.replace('o', '')
        res = res.replace('O', '')
    return res


def generate_password(length, chars):
    res = ''
    for _ in range(length):
        res += chars[random.randint(0, len(chars)) - 1]
    return res


DIGITS = '0123456789'
LOW_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UP_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'
chars = ''
while True:
    try:
        amount_pw = int(input('Укажите количество паролей для генерации: '))
        len_pw = int(input('Укажите длину одного пароля: '))
        break
    except ValueError:
        print('Введите корректные числа')
digits_on = input('Включать ли цифры 0123456789? (Введите "Y" для подтверждения) ')
up_on = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (Введите "Y" для подтверждения) ')
low_on = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (Введите "Y" для подтверждения) ')
punctuation_on = input('Включать ли символы !#$%&*+-=?@^_? (Введите "Y" для подтверждения) ')
except_on = input('Исключать ли неоднозначные символы il1Lo0O? (Введите "Y" для подтверждения) ')

chars = assembly(digits_on, up_on, low_on, punctuation_on, except_on, chars)

print(*[generate_password(int(len_pw), chars) for _ in range(int(amount_pw))])
