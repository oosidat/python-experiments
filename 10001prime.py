def isprime(n):
    testfac = 2
    while testfac < n:
        if n % testfac == 0:
            return False
        else: testfac = testfac + 1
    return True

def thousprime():
    primecount = 0
    while primecount < 10001:
        starter = 2
        if isprime(starter) == True:
            starter = starter + 1
            primecount = primecount + 1
        else: starter = starter + 1
    return starter

thousprime()
