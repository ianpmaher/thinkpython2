"""
Ex 8-5: A Caesar cypher is a weak form of encryption that involves “rotating” 
each letter by a fixed number of places. 
To rotate a letter means to shift it through the alphabet, 
wrapping around to the beginning if necessary, so 
A rotated by 3 is D and Z rotated by 1 is A.
To rotate a word, rotate each letter by the same amount. 
For example, “cheer” rotated by 7 is “jolly” and 
“melon” rotated by -10 is “cubed”. 
In the movie 2001: A Space Odyssey, the ship computer is called HAL, which is IBM rotated by -1. 

Write a function called rotate_word that takes a string and an integer as parameters,
and returns a new string that contains the letters from the original string rotated by the given amount.
You might want to use the built-in function ord, which converts a character to a numeric code, 
and chr, which converts numeric codes to characters. Letters of the alphabet are encoded in 
alphabetical order, so 
> ord('c') - ord('a') = 2     #because c is the two-eth letter of the alphabet
"""
def stringforwards(stringHere):
    for character_index in stringHere:
        print(character_index) # print each character one at a time from the string

# I took this directly from Allen Downey's code because I couldn't figure it out
# "The numeric codes of uppercase letters are different."
def rotate_letter(letter, n):
    """Rotates a letter by n places.  Does not change other chars.
    letter: single-letter string
    n: int
    Returns: single-letter string
    """
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)

def rotate_word(word, numba):
    # rotates a letter by 'numba' places a la caesar cypher
    # letter : single letter string
    rotated_word = ''
    for letter in word:
        rotated_word += chr(ord(letter) + numba)
    return rotated_word

if __name__ == '__main__':
    print(rotate_word('IBM', -1))
    print(rotate_word('sleep', 9))
    print(rotate_word('melon', -10))
    print(rotate_word('cheer', 7))
   
"""
def prompting():
    a = input("Type your word to rotate: \n")
    b = input("Type your number to encrypt the word by: \n")
    
    print(rotate_word(str('a'), int(b)))

prompting()
"""
# ^ I want to figure out how to make this interactive, it is a cool idea.