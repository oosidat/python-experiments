## Project Euler - Question 2
## Sum of all the values of fib smaller than 4M

def fib(n):
    if n < 0: return 0
    if (n == 1 or n == 2): return n
    thisfib = 0
    i = 3
    pre1 = 1
    pre2 = 2
    while (i <= n):
        thisfib = pre1 + pre2
        pre1 = pre2
        pre2 = thisfib
        i = i + 1
    return thisfib

tot = 0
y = 1
thisfib = fib(y)
while (thisfib <= 4000000):
    if (thisfib%2) == 0:
        tot = tot + thisfib
    y = y + 1
    thisfib = fib(y)
print tot
