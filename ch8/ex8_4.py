"""
The following fucntions are all INTENDED to check whether a string 
contains any lowercase letters, but at least some of them are wrong.
For each function, describe what the function actually does (assuming 
that the parameter is a string.)
"""

def any_lowercase1(s):
    # checks only the first letter in string if lowercase or not 
    # returns boolean
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
    # checks if string 'c' is lowercase or not
    # returns 'True' every time regardless
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    # checks if each letter in string is lowercase or not 
    # assigns boolean true/false value to the variable 'flag'
    # new value assigned to 'flag' variable with each letter
    # returns boolean value of calling islower() method on only 
    # the last letter of the given string
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    # checks if there is ANY lowercase letter in the string, returns Boolean
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag
    
def any_lowercase5(s):
    # checks every letter if it is not lowercase
    # returns boolean if all the letters in the string are lowercase or not 
    for c in s:
        if not c.islower():
            return False
    return True

print(any_lowercase1('America'))
print(any_lowercase2('America'))
print(any_lowercase3('America'))
print(any_lowercase4('America'))
print(any_lowercase5('America'))