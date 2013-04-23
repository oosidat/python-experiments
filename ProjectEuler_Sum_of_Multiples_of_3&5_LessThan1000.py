## Project Euler - Question 1
## Finding sum of all natural numbers less than 1000, which are multiples of
## 3 or 5
## 1000 is not included

def sum_1000():
    n = 0
    sum_1K = 0
    while n < 1000:
        if (n%3 == 0) or (n%5 == 0):
            sum_1K = sum_1K + n
            n = n+1
        else: n = n + 1
    return sum_1K

print sum_1000()
