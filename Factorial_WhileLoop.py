## Factorial Using while loops
## Computing a factorial + function to create a list of factorial values from a list of values.

def factorial(n):
    fac_so_far = 1
    while n >= 1:
        fac_so_far = n * fac_so_far
        n = n - 1
    return fac_so_far

def make_fac_list(lst):
    return map(factorial, lst)