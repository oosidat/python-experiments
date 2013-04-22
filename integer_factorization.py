## Integer Factorization

from random import randint
import math
import gmpy

n=12345679014814814815185185185234567901240740740741481481481567901234577777835803333339135876543790129629687654814820617320988234570370428395185190987717459
m=99999999999999999999999999999999999999999999999999999999999999999999999999999
digits = int(math.log10(m))+1



def checkmodzero():
    i = 1
    while i < (2**256 - 2**255):
        x = randint(0,m)
        if (gmpy.is_prime(x) == True): y = x
        else: y = gmpy.next_prime(x)
        if (n % y == 0):
            q = n / y
            print "Success, p is %d" %y
            print "and q is %d" %q
            return y
        else: print "%d tested %d" %(i,y)
        i = i + 1
    return -1

print digits
