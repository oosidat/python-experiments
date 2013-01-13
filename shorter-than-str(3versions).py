def shorter_than(los,n):
    return filter (lambda s: len(s) < n,los)


def shorter_than_while(los,n):
    pos = 0 #init
    num_short_str = 0 #init
    while len(los) > pos:
        if len(los[pos]) < n:
            num_short_str = num_short_str + 1 #update
        pos = pos + 1
    return num_short_str

def shorter_than_for(los,n):
    numshortstr = 0
    for s in los:
        if len(s) < n:
            numshortstr = numshortstr + 1
    return numshortstr