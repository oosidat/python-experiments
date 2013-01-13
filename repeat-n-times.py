## repeat n_times

## if n_times() is called and the user enters 3
## wewe will print out 3 on three lines.
def n_times():
    ## read user input
    n = int(raw_input("enter n:"))
    helper (n,n)
    
## helper
def helper(n, times_left):
    ## base case
    if times_left == 0:
        return
    ## recursive case
    else:
        print n
        helper(n, times_left - 1)
        
n_times()
