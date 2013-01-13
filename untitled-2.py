import os
print os.getcwd()

f = file('ascii.txt', 'w')
f.write ('ASCII file \n')

for i in range(0, 2**7):
    f.write(chr(i) + ' ' + str(i) + "\n")
f.close()