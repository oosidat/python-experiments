## given 3 digit num, produce sum of three digits

def sum_digits(numx):
    third = numx % 10
    first = numx / 100
    second = (numx % 100) / 10
    return first + second + third

print sum_digits(763)
print sum_digits(999)
print sum_digits(876)