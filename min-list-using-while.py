def min_while(lstx):
    min_val = lstx[0]
    for item in lstx:
        if item < min_val:
            min_val = item
    return min_val

lsta = [1.5]

print min_while(lsta)