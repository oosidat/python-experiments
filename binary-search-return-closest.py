def binary_search (L,w):
    beg = 0
    end = len(L)
    while abs(beg - end) > 1:
        mid = (end + beg)/2
        if L[mid] == w:
            return mid
        elif L[mid] > w:
            end = mid
            print "beg1=", beg, "end=", end
        else: 
            beg = mid
            print "beg2=", beg, "end=", end
    if abs(L[end] - w) < abs(L[beg] - w):
        return end
    else: return beg

#lista = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]

#print binary_search(lista, 8.5)

listb = [1.0, 3.0, 5.0]

print binary_search(listb, 0.9)
print binary_search(listb, 2.0)
print binary_search(listb, 2.5)