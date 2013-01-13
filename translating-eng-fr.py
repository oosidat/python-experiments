eng = {1:'one', 10:'ten', 21:'twenty-one', 2:'two', 99: 'ninety-nine'}
fr = {2: 'deux', 10:'dix', 1:'un', 3:'trois', 21:'vingt-et-un'}

class Translation:
    'Fields: english, french'
    
def create_trans(e,f):
    combined = {} # empty dictionary
    for  n in e.keys():
        t = Translation() # constructor
        t.english = e[n]
        if f.has_key(n):
            t.french = f[n]
        else:
            t.french = 'unknown'
        combined[n] = t # object of class Translation
    return combined

new_d = create_trans(eng,fr)

for n in new_d.keys():
    print n, new_d[n].english, new_d[n].french