## Project Euler - Question 3
## Find largest prime factor of i

i = 600851475143
j = 59569

def find_prime(x):
    L = []    
    n = 2
    while n <= (x**0.5):
        if (x % n) == 0:
            L.append(n)
        n = n + 1
    return L

print find_prime(i)
print find_prime(j)