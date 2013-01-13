def ispalindrome5(x):  
    z = str(x)  
    l=len(z)/2  
    if z[:l]==z[-l:][::-1]:  
        return 1  
    return 0

def ispalindrome(x):
    if str(x) == str(x)[::-1]:
        return 1
    else: return 0