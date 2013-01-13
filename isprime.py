def isprime(n):
    if n == 2: return 1
    if n % 2 == 0: return 0
    max = n**0.5+1
    i = 3
    while i <= max:
        if n % i == 0: return 0
        i+=2
    return 1


def prlst(m):
    L = [2]
    count = 1
    x = 3
    while count < m:
        if(isprime(x) == True):
            L.append(x)
            count = count + 1
            x = x + 2
        else: x = x + 2
    print "Length of L is %d" % (len(L))
    return L

print prlst(10001)