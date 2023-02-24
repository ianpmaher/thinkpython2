def first(word):
    """returns the first letter of a string"""
    return word[0]

def last(word):
    """returns the last letter of a string"""
    return word[-1]

def middle(word):
    """returns letters of a string EXCEPT FOR the first and last letters"""
    return word[1:-1]

def is_palindrome(word):
    """returns True if it is a palindrome"""
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))

'''
print(is_palindrome('allen'))
print(is_palindrome('bob'))
print(is_palindrome('otto'))
print(is_palindrome('redivider'))
'''

print(is_palindrome(str(input())))