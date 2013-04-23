## pythagorean triplets... A highly inefficient algorithm...

import math

def pytfinder():
    count = 500
    for x in range(1,count):
        for y in range(x + 1,count):
            for z in range(y + 1,count):
                if z*z == y*y + x*x:
                    if x + y + z == 1000:
                        print y, z, x
    print "Testing complete"

#print "Testing"
#pytfinder()
print 375*425*200