def repeat_yes():
    x = raw_input("Do you want to continue? (Y/N): ") ## User input
    while x == "Y": ## Checks if x == :"Y"
        x = raw_input("Do you want to continue? (Y/N): ") ## If it is, asks for User to input again
    print "Thank you for your patience... :P" 

repeat_yes()