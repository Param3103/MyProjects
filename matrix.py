num1 = [1, 2, 3, 4]
# convert above set into 2-by-2 matrix
num2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# convert above set to 3-by-3 matrix
#generalise to n^2
def matrix(numbers):
    size = len(numbers)
    length = size ** 0.5 # matrix has dimensions length-by-length
    lengthtemp = length
    length = int(length)
    if length != lengthtemp: 
        return('Error!')
    matrix = []
    for i in range(length):
        matrix.append([])
    x = 0
    for i in range(length):
        for j in range(length):
            matrix[i].append(numbers[x])
            x += 1
    return(matrix)

print(matrix(num2))


