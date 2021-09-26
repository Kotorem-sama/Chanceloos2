def Octal(number):
    square = 0
    outcome = ''
    while (number / (8 ** (square + 1))) >= 1:
        square += 1
    for i in range(0, square):
        rsquare = square - i
        thing = number // (8 ** rsquare)
        outcome += str(thing)
        number -= thing * (8 ** rsquare)
    return outcome + str(number)

def Binary(number):
    square = 0
    outcome = ''
    while (number / (2 ** (square + 1))) >= 1:
        square += 1
    for i in range(0, square):
        rsquare = square - i
        thing = number // (2 ** rsquare)
        outcome += str(thing)
        number -= thing * (2 ** rsquare)
    return outcome + str(number)

def Hexadecimal(number):
    hexa = '0123456789ABCDEF'
    square = 0
    outcome = ''
    while (number / (16 ** (square + 1))) >= 1:
        square += 1
    for i in range(0, square):
        rsquare = square - i
        thing = number // (16 ** rsquare)
        outcome += hexa[thing]
        number -= thing * (16 ** rsquare)
    return outcome + hexa[number]