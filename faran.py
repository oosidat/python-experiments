## Largest multiple

no_multiple = 'fail'
possible = 'possible'

def larmultiple(low,up,div):
    if up < low:
        return no_multiple
    else:
        if up%div == 0:
            return up
        else: return (larmultiple(low,up-1,div))

print larmultiple(15,24,5)