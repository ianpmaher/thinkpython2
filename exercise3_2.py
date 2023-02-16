# A function object is a value you can assign to a variable or pass as an argument.
# For example, do_twice is a function that takes a function object as an argument and calls it twice:
def do_twice(f, g):
    f(g)
    f(g)
# Here's an example that uses do_twice to call a function named print_spam twice
def print_twice(s):
    print(s)
    print(s)

# this is answer to above
# do_twice(print_twice, 'spam')

# modify do_twice so that it takes two arguments, a function object, and a value, and 
# and calls the function twice, passing the value as an argument.

# define a new function called do_four that takes a function object and a value and 
# calls the function four times, passing the value as a paramter.
# There should be only two statements in the body of this function, not four.

def do_twice(func, arg):
    """Runs a function twice.
    func: function object
    arg: argument passed to the function
    """
    func(arg)
    func(arg)


def print_twice(arg):
    """Prints the argument twice.
    arg: anything printable
    """
    print(arg)
    print(arg)


def do_four(func, arg):
    """Runs a function four times.
    func: function object
    arg: argument passed to the function
    """
    do_twice(func, arg)
    do_twice(func, arg)


do_twice(print, 'spam')
print('')

do_four(print, 'spam')