## dropbox challenge

def finder():
    starter = 10000
    while starter < 100000:
        A = str(starter)
        a = int(A[0])
        b = int(A[1])
        c = int(A[2])
        d = int(A[3])
        e = int(A[4])
        startersum = a + b + c + d + e
        if (startersum == 26) and (a * b == 24) and (d == 0.5 * b) and (d + e == a + c) and (b > e):
            print starter
            return starter
        else:
            starter = starter + 1

        
    