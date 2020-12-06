def leapyear(year):
    isleapyear = False
    if year % 4 == 0:
        isleapyear = True
    if year % 100 == 0:
        isleapyear = False
    if year % 400 == 0:
        isleapyear = True
    if isleapyear == True:
        return(str(year) + " is a leap year")
    return(str(year) + " is not a leap year")

def factorial(num):
    if type(num) is not int:
        return('Error')
    elif num < 0:
        return('Error')
    elif num == 0:
        return(1)
    elif num >= 1:
        temp = 1
        for i in range(1, n + 1):
            temp *= i
        return(temp)
def Fib(num):
    fibb = []
    while len(fibb) < num:
        if len(fibb) == 0:
            fibb.append(0)
        elif len(fibb) == 1:
            fibb.append(1)
        else:
            fibb.append(fibb[-1] + fibb[-2])
    return(fibb)
def numberofdigits(num):
    dig = 0
    if num == 0:
        dig = 1
    while num >= (10 ** dig):
        dig += 1
    return(dig)
def numberofdigits1(num):
    dig = 0
    for i in str(num):
        dig += 1
    return(dig)

def isArmstrong(num): #sum of digits = number
    dig = numberofdigits1(num)
    sums = 0
    for i in str(num):
        i = int(i)
        sums += i ** dig
    if sums == num:
        return(str(num) + " is an Armstrong number")
    return(str(num) + " is not an Armstrong number")
