## Binary Search Through Iteration

def binary_search (L,w):
    beginning = 0
    end = len(L)
    while beginning < end:
        mid = (beginning + end)/2
        if L[mid] == w:
            print "Found it! :" + str(w)
            return True
        elif L[mid] < w:
            beginning = mid
        else:
            end = mid - 1
    print str(w) + "Not Found in List"
    return False

def binary_search_return_closest (L,w):
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

## Testing
list1 = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]


list2 = [1.0, 3.0, 5.0]
print binary_search(list1, 4.5)
print binary_search_return_closest(list2, 0.9)
print binary_search_return_closest(list2, 2.0)
print binary_search_return_closest(list2, 2.5)