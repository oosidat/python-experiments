## echo

def echo():
    x=raw_input("Enter Something:")
    if x=="shut up!":
        return"Sorry..."
    else:
        print x
        return echo()
    
echo()
