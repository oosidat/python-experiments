## palindrome

def palindrome(s):
    if len(s) < 2:
        return True
    if s[0] != s[len(s)-1]:
        return False
    return palindrome(s[1:len(s) - 1])

print palindrome('oso')
print palindrome('osa')
