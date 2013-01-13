import os

def str_to_house(s):
    parts = s.split()
    

house_data = file('Housing_kitchener.txt') # default = 'r'
houslist = map(str_to_house, house_data.readline())
house_data.close() # close immediately

for h in houselist:
    print "%d %s, %s"%(h.number, h.address, h.city())

house_numbers = file('Numbers.txt', 'w')
for h in houselist:
    Output = "%d \n" % (h.number*5)
    house_numbers.write(Output)

house_numbers.close()