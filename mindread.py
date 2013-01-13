##
##
## Write a function mindread, which consumes an
## integer starter between

def mindread (starter):
    ones_digit = starter%10
    tens_digit = starter/10
    sum = ones_digit + tens_digit
    ans = starter - sum
    return ans

print "test1"
print mindread(76) == 63


## How to print?
## print