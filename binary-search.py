def binary_search (L,w):
    beginning = 0
    end = len(L)
    while beginning < end:
        mid = (beginning + end)/2
        if L[mid] == w:
            print "Found it! :" + str(w)
            return True
        elif L[middle] < w:
            beginning = mid + 1
        else:
            end = mid - 1
    print str(w) + "Not Found in List"
    return False