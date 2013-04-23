## A few versions of detecting a palindrome, with different returns.

def ispalindrome1(x):  
    z = str(x)  
    l=len(z)/2  
    if z[:l]==z[-l:][::-1]:  
        return 1  
    return 0

def ispalindrome2(x):
    if str(x) == str(x)[::-1]:
        return 1
    else: return 0

## recursive version from CS116
def palindrome(s):
    if len(s) < 2:
        return True
    if s[0] != s[len(s)-1]:
        return False
    return palindrome(s[1:len(s) - 1])