import.math

## prime-while

def prime(n):
    testfac = 2
    while testfac < n:
        if n % testfac == 0:
            return False
        else: testfac = testfac + 1
    return True

print prime(21)
print prime(23)