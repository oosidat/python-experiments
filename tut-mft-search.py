## Tutorial 10

def mft_search(lst,searches):
    for item in searches:
        found = False
        n = 0
        while (not found) and n < len(lst):
            if lst[n] == item:
                print item, "was found"
                lst.insert(0, lst.pop(n))
                found = true
            else:
                n += 1
        if found == False:
            print item, "was not found"
            