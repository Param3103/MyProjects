def half_diamond(size, row):
    temp = size
    # hello this is a comment
    while temp > 1:
        if temp > row:
            print(' ', end = ' ')
            temp -= 1
        else:
            print(temp, end = ' ')
            temp -= 1
    while temp <= size:
        if temp > row:
            print(' ', end = ' ')
            temp += 1
        else:
            print(temp, end = ' ')
            temp += 1
def diamond(size):
    row = 1
    while row < size:
        half_diamond(size, row)
        row += 1
        print('')
    while row > 0:
        half_diamond(size, row)
        row -= 1
        if row != 0:
            print('')
print(diamond(5))