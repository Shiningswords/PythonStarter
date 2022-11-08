import random


def is_valid(num, diapason):
    try:
        if 1 <= int(num) <= int(diapason):
            return True
        else:
            return False
    except ValueError:
        return False


def set_diapason():
    while True:
        diapason = input('Будет загадано число в диапазоне от 1 до ... (введите число): ')
        if is_valid(diapason, diapason):
            diapason = int(diapason)
            return diapason
        else:
            print('Введите корректное число!\n')


print('\nДобро пожаловать в игру "ЧИСЛОВАЯ УГАДАЙКА"!\n')
max_num = set_diapason()
answer, counter = random.randint(1, max_num), 1
while True:
    attempt = input(f'Введите число от 1 до {max_num}: ')
    if is_valid(attempt, max_num):
        attempt = int(attempt)
        if attempt < answer:
            print(f'Попытка номер {counter}: Ваше число меньше загаданного, попробуйте еще разок\n')
            counter += 1
        elif attempt > answer:
            print(f'Попытка номер {counter}: Ваше число больше загаданного, попробуйте еще разок\n')
            counter += 1
        else:
            print(f'\nВсего попыток: {counter}. Вы угадали, поздравляем!')
            decision = input('\nХотите сыграть ещё раз? '
                             '(Введите "Y" для повторной игры и любой другой символ для выхода) ')
            if decision == 'Y':
                max_num = set_diapason()
                counter = 1
            else:
                break
    else:
        print(f'\nА может быть все-таки введем целое число от 1 до {max_num}?')
print('\nСпасибо, что играли в числовую угадайку. Еще увидимся...')
