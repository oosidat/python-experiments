"""This module is used for testing in CS 116.
It contains five functions and two constants:
 - input_list is a list for use with our_input.
 - expected_screen is printed by expect and within.
 - set_input_list is a function which sets the value of
   input_list.
 - set_expected_screen is a function which sets the value
   of expected_screen.
 - expect is a function for testing exact values.
 - within is a function for testing floating point values.
 - our_input is a function which reads in input from
   either the keyboard or from the beginning of input_list.
"""

input_list = []
expected_screen = ""

def set_input_list(lst):
    """Sets input_list to be equal to lst."""
    global input_list
    input_list = lst

def set_expected_screen(string):
    """Sets expected_screen to be equal to string."""
    global expected_screen
    expected_screen = string

def our_input(prompt=""):
    """
    Produces a string from either keyboard input or input_list.
    
    Produces a string. If input_list is empty, our_input
    calls raw_input and returns its value. If input_list is
    non-empty, its first value is cast to a string, removed
    from input_list, and returned.

    out_input has an optional argument, prompt, which will
    be displayed to the user before they enter any keyboard
    keyboard input (if raw_input is called).
    """
    if input_list:
        return str(input_list.pop(0))
    else:
        return raw_input(prompt)

def expect(name, function_call, expected_value):
    """
    Testing function for equality.
    
    IMPORTANT: This function should not be used if function_call
    produces a floating point number; in that case, use check.within
    
    Compares the value produced by function_call to expected_value.
    If the two values are equal (using ==), prints "Passed";
    if the two values are not equal, prints
    "FAILED; expected [expected_value], saw [function_call]"

    If function_call prints any values, they will be printed before
    the Passed/Failed message. If the state variable expected_screen
    is non-empty, it will also be printed before the Passed/Failed
    message. The equality (or inequality) of expected_screen and the
    print statements within the function have no effect on what is
    printed in the Passed/Failed message.
    """
    global expected_screen
    if expected_screen:
        print ("%s: Actual screen output is above, " % name) +\
              "description of expected screen output is below."
        print expected_screen
        print ""
    if function_call == expected_value:
        print "%s: Passed" % name
    else:
        print "%s: FAILED; expected %s, saw %s" \
              % (name, expected_value, function_call)
    if expected_screen:
        expected_screen = ""
        print "\n----------\n"

def within(name, function_call, expected_value, acceptable_range):
    """
    Testing function for floating point numbers.
    
    IMPORTANT: This function should only be used if function_call
    produces a floating point number; otherwise, use check.expect
    
    Compares the number produced by function_call to expected_value.
    If the two numbers are within acceptable_range of each other
    (ie the absolute value of their difference is less than
    acceptable_range), prints "Passed"; otherwise, prints
    "FAILED; expected [expected_value], saw [function_call]"

    If function_call prints any values, they will be printed before
    the Passed/Failed message. If the state variable expected_screen
    is non-empty, it will also be printed before the Passed/Failed
    message. The equality (or inequality) of expected_screen and the
    print statements within the function have no effect on what is
    printed in the Passed/Failed message.
    """
    global expected_screen
    if expected_screen:
        print ("%s: Actual screen output is above, " % name) +\
              "description of expected screen output is below."
        print expected_screen
        print ""
    if abs(function_call-expected_value) < acceptable_range:
        print "%s: Passed" % name
    else:
        print "%s: FAILED; expected %s, saw %s" \
              % (name, expected_value, function_call)
    if expected_screen:
        expected_screen = ""
        print "\n----------\n"

