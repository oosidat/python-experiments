## Project-Euler - Question 4
## Produce largest number which is a palindrome and a product of 2 3-digit numbers.

def ispalindrome(x):
    if str(x) == str(x)[::-1]:
        return True
    else: return False

def produce_list():
    L = []
    for x in range(100, 999):
        for y in range(100, 999):
            if ispalindrome(x*y) == True:
                L.append(x*y)
    return L

print max(produce_list())