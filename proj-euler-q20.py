## Project Euler - Question 20
## Sum of all digits of 100!

import math

def sum_long():
    n = str(math.factorial(100))
    i = 0
    tot = 0
    while i < len(n):
        tot = tot + int(n[i])
        i = i + 1
    return tot

print sum_long()