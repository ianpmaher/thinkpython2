# the built-in funciton eval takes a string and evaluates it using the Python interpreter
# for exxample, 
# >>> eval('1 + 2 * 3')
# 7
# >>> import math
# >>> eval('math.sqrt(5)')
# 2.2360679774997898
# >>> eval('type(math.pi)')
# <class 'float'>
# Write a function called eval_loop that iteratively prompts the user, takes the resulting input and 
# evaluates it using eval, and prints the result. It should continue until the user enters 'done', 
# and then return the value of the last expression it evaluated.

def eval_loop():
    """Iteratively prompts the user, takes the resulting input and evaluates it
    using eval, and prints the result.
    It should continue until the user enters 'done', and then return the value of
    the last expression it evaluated.
    """
    result = None
    while True:
        user_input = input('>> ')
        if user_input == 'done':
            break 
        print(user_input)
        result = eval(user_input)
        print(result)
    return result

eval_loop()