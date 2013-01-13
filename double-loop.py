## double_loop: An example of a nested loop... with an outer and an inner loop

## Nested For Loops
## For every iteration of outerloop, the inner loop goes through all
## iterations of itself. Then goes to the next iteration of the outerloop.

## Also works for while loops.

def double_loop(n, m):
    for i in range(0,n):
        for j in range(0,m):
            print i, j