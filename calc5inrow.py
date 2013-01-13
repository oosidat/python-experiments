def calculator(y):
    x1 = 0
    x2 = x1 + 1
    x3 = x1 + 2
    x4 = x1 + 3
    x5 = x1 + 4
    maxsofar = 0
    while x5 != (len(y)):
        product = int(y[x1]) * int(y[x2]) * int(y[x3]) * int(y[x4]) * int(y[x5])
        if product < maxsofar:
            maxsofar = product
            x1 = x1 + 1
        else: x1 = x1 + 1
    return maxsofar

print calculator("123456")