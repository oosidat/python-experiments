## Project Euler - Question 6
## Difference between Sum of squares and square of sum

lst100 = range(1,101)
print lst100

def sum_squares():
    return sum(map (lambda x: x**2, lst100))

def square_sum():
    return (sum(lst100))**2

print sum_squares()

print square_sum()

print abs(sum_squares() - square_sum())