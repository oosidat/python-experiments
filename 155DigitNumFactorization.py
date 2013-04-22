import os

primenumbers = []
#for line in open('C:\Users\Osama Sidat\Documents\GitHub\python-experiments\digitPrimes.txt'):
#    primenumbers.append(long(line[0:line.index(' (')]))

for line in open('C:\Users\Osama Sidat\Documents\GitHub\python-experiments\digitPrimes2.txt'):
    primenumbers.append(long(line))

n=12345679014814814815185185185234567901240740740741481481481567901234577777835803333339135876543790129629687654814820617320988234570370428395185190987717459


for i in primenumbers:
    if ((n % i) == 0): print i

print len(str(n))
