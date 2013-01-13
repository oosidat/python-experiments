## takes in a list and a target, produces the index of the number closest to target.

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

list1 = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]

print binary_search(list1, 4.5)