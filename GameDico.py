from random import randint

balans = 100
gameover = False
while not gameover and balans > 0:
    print('Ваш баланс: ', balans)
    while True:
        option1 = input('Введите число, на которое хотите поставить, от 2 до 12: ')
        if str.isnumeric(option1):  # проверка на ввод числа
            option = int(option1)
            if option in range(2, 13):  # проверка на диапазон
                break  # выход из цикла while True для числа
            print('Ставка должна быть в диапазоне от 2 до 12!')
        else:
            print('Неверный формат ввода данных. Вводите только числа!')
    while True:
        stavka1 = input('Введите сумму ставки: ')
        if str.isnumeric(stavka1):  # проверка на ввод числа
            stavka = int(stavka1)
            if stavka <= balans:
                break  # выход из цикла while True для ставки
            print('Недостаточно баланса для такой ставки!')
        else:
            print('Неверный формат ввода данных. Вводите только числа!')
    balans -= stavka
    num1 = randint(1, 6)
    num2 = randint(1, 6)
    summa = num1 + num2
    print('Выпали числа {} и {}. Сумма = {}'.format(num1, num2, summa))
    if summa == option:
        print('Везунчик! Вы выиграли в четыре раза больше очков, чем сделанная ставка!')
        balans += stavka * 5  # возвращаем ставку (balans -= stavka) + выигрыш (stavka*4)
    elif (summa < 7 and option < 7) or (summa > 7 and option > 7):
        print('Отлично! Вы выиграли свою ставку!')
        balans += stavka * 2  # возвращаем ставку (balans -= stavka) + выигрыш (stavka)
    else:
        print('К сожалению, Вы проиграли ставку!')
    gameover = bool(input('Если хотите выйти, введите любой символ. Если хотите продолжить - нажмите Enter: '))
print('Игра окончена. У Вас закончились баллы или Вы захотели выйти из игры.')
