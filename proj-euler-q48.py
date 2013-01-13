## Project Euler - Question 48
## Last 10 digits of 1^1 + 2^2 + .... + 1000^1000

def find_sum_1000():
    n = 1
    tot = 0
    while n <= 1000:
        tot = tot + (n**n)
        n = n + 1
    string_tot = str(tot)
    return string_tot[len(string_tot)-10:len(string_tot)]

print find_sum_1000()