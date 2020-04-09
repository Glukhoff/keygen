import random

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


def quantity_tokens():
    while True:
        try:
            quantity = int(input('Введите необходимое колличество токенов: '))
            break
        except:
            print('Введено не корректное значение')
            continue
    return quantity


def gentoken():
    counter = 0
    symbol = (5, 10, 15, 20)
    token = ''
    for _ in range(25):
        token += alphabet[random.randint(0, 35)]
        counter += 1
        if counter in symbol:
            token += '-'
            continue
    return token


f = open('/Users/glukhovsergey/Desktop/key.txt', 'w')
for _ in range(quantity_tokens()):
    f.write(gentoken() + '\n')
f.close()
