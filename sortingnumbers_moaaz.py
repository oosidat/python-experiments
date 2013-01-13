## Sorting x , y , z from smallest to largest

x = 3
y = 2
z = 1

tmp = max(x,y)
x = min(x,y)
y = tmp


tmp = max(y,z)
y = min(y,z)
z = tmp

tmp = max(x,y)
x = min(x,y)
y = tmp


print (x)
print (y)
print (z)
