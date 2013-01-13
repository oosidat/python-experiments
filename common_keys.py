## commonkeys2

d_1 = {10: 2, 100: 3, 1: 0, 34: 2}
d_2 = {1: 'a', 34: 'b', 200: 'c'}

def common_keys2(d1,d2):
    in_both = []
    keys1 = d1.keys()
    for k in keys1: # goes through every key in d1
        if d2.has_key(k): # if k is in d2, add to in_both list
            in_both.append(k)
    return in_both

def common_keys(d1,d2):
    keys1 = d1.keys() # list of keys in d1
    keys2 = d2.keys() # list of keys in d2
    in_both = filter(lambda x: x in keys1, keys2)
    return in_both

print common_keys2(d_1,d_2)
print common_keys(d_1,d_2)