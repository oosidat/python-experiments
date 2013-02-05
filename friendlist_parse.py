## list parser, for Facebook
import os
#myfile = file('C:\Users\Osama Sidat\Documents\Python Projects\listoffriends.txt', 'r')

importlist =[]
for line in open('C:\Users\Osama Sidat\Documents\Python Projects\listoffriends.txt'):
  importlist.append(line)


#print importlist
#if i = 1 mod 4

exportlist = []

for i in range(0, len(importlist)):
    if ((i % 4) == 1):
        exportlist.append(importlist[i])

print exportlist
