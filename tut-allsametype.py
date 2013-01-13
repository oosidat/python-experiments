## allsame

def all_same_type(alst):
    if len(alst) < 2:
        return True
    t1 = type(alst[0])
    bad = filter (lambda x: type(x) != t1, alst)
    return len(bad) == 0

print all_same_type([1, 2, 3])
print all_same_type([1, 2, "happy!"])