## white-space removal

import string

a = "  hello   kitty  123  "
print string.join(a.split(), " ")
print a.split()

## can also be written without importing string as:
print " ".join(a.split())
## This is the simplest version for rewriting a string which has extra spaces
## in them, as long as the extra spaces are between full formed words.
## For example, the string "I am ," would be returned as "I am ," and NOT "I am,"