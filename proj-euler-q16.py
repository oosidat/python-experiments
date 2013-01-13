## Project Euler - Question 16
## Sum of all digits of 2**1000

def sum_long():
    n = str(2**1000)
    i = 0
    tot = 0
    while i < len(n):
        tot = tot + int(n[i])
        i = i + 1
    return tot

print sum_long()