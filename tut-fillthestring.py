## fill_the_string

def fill_the_string(s,n):
    return (n/len(s)) * s + s[ :n%len(s)]

print fill_the_string('love',12)
print fill_the_string("truth",12)
print fill_the_string('love',3)

