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
    i = 3
    while i < m:
        if(isprime(i) == True):
            L.append(i)
            i = i + 2
        else: i = i + 2
    print "Length of L is %d" % (len(L))
    return L

print sum(prlst(2000000))