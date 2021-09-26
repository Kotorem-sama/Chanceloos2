alpha = 'abcdefghijklmnopqrstuvwxyz'

def thingmaker(size, actualsize):
    midpart = ''
    if size == 1:
        return alpha[actualsize - 1]
    for i in range(0, size):
        midpart += alpha[actualsize - 1 - i] + '-'
        if i == size - 1:
            j = 0
            while j < size - 1:
                midpart += alpha[actualsize - (i - j)]
                if j != size - 2:
                    midpart += '-'
                j += 1
    return midpart

def print_rangoli(size):
    end = ''
    midpart = thingmaker(size % len(alpha), size % len(alpha)) + '\n'
    length = len(midpart) - 1
    for i in range(1, size % len(alpha)):
        end += thingmaker(i, size % len(alpha)).center(length, '-') + '\n'
    end += midpart
    for i in range(1, size % len(alpha)):
        end += thingmaker(size % len(alpha) - i, size % len(alpha)).center(length, '-') + '\n'
    print(end[0:-1])

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)