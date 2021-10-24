"""
1) print this
1 2 3 4
1 2 3
1 2
1
"""
def topleft(x):
    while x >= 1:
        for i in range(1, x):
            print(i, end = ' ')
        print(x)
        x -= 1

"""
2) print this
1
1 2
1 2 3
1 2 3 4
"""
def bottomleft(x):
    i = 1
    while i <= x:
        j = 1
        while j < i:
            print(j, end = ' ')
            j += 1
        print(i)
        i += 1
"""
3)print this

1 2 3 4 3 2 1
1 2 3   3 2 1
1 2       2 1
1           1
"""
def toplefttopright(x):
    for i in range(x):
        j = 1
        while j <= x:
            if j <= (x - i):
                print(j, end = ' ')
                j += 1
            else:
                print(' ', end = ' ')
                j += 1
        j -= 2
        while j > 0:
            if j <= (x - i):
                print(j, end = ' ')
                j -= 1
            else:
                print(' ', end = ' ')
                j -= 1
        print('')
"""
4)print this
1 2 3 4
1 2 3
1 2
1
1 2
1 2 3
1 2 3 4
"""
def topleftbottomleft(x):
    y = x
    while x >= 1:
        for i in range(1, x):
            print(i, end = ' ')
        print(x)
        x -= 1
    i = 2
    while i <= y:
        for j in range(0, i):
            if j != 0:
                print(j, end = ' ')
        print(i)
        i += 1
"""
5)print this

1 2 3 4 3 2 1
1 2 3   3 2 1
1 2       2 1
1           1
1 2       2 1
1 2 3   3 2 1
1 2 3 4 3 2 1
"""
def emptydiamond(x):
    for i in range(0, x):
        j = 1
        while j <= x:
            if j <= (x - i):
                print(j, end = ' ')
                j += 1
            else:
                print(' ', end = ' ')
                j += 1
        j -= 2
        while j > 0:
            if j <= (x - i):
                print(j, end = ' ')
                j -= 1
            else:
                print(' ', end = ' ')
                j -= 1
        print('')
    for i in range(2, (x + 1)):
        j = 1
        while j <= x:
            if j <= i:
                print(j, end = ' ')
                j += 1
            else:
                print(' ', end = ' ')
                j += 1
        j -= 2
        while j > 0:
            if j <= i:
                print(j, end = ' ')
                j -= 1
            else:
                print(' ', end = ' ')
                j -= 1
        print('')
"""
6)print this
      1
    2 1
  3 2 1
"""
def bottomrighttriangle(x):
    j = 1
    while j <= x:
        i = x
        while i > 0:
            if i > j:
                print(' ', end = ' ')
                i -= 1
            else:
                print(i, end = ' ')
                i -= 1
        j += 1
        print('')


"""
7)print this
     1
   2 1 2
 3 2 1 2 3
   2 1 2
     1

"""
def diamond(x):
    m = 1
    while m < x:
        j = x
        while j > 1:
            if j > m:
                print(' ', end = ' ')
                j -= 1
            else:
                print(j, end = ' ')
                j -= 1
        while j <= x:
            if j > m:
                print(' ', end = ' ')
                j += 1
            else:
                print(j, end = ' ')
                j += 1
        m += 1
        print('')
    while m > 0:
        j = x
        while j > 1:
            if j > m:
                print(' ', end = ' ')
                j -= 1
            else:
                print(j, end = ' ')
                j -= 1
        while j <= x:
            if j > m:
                print(' ', end = ' ')
                j += 1
            else:
                print(j, end = ' ')
                j += 1
        m -= 1
        if m != 0:
            print('')
