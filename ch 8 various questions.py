# Chapter 8 Various Questions

# as an exercise, write a function that takes a string as an argument and 
# displays the letters backward, one per line
def stringBackwards(stringHere):
    i = len(stringHere) - 1
    while i >= 0:
        letter = stringHere[i]
        print(letter)
        i = i - 1

def ducklings(stringhere):
    prefixes = 'JKLMNOPQ'
    suffix = 'ack'
    for letter in prefixes:
        if letter == "O" or letter == "Q":
            print(letter + "u" + suffix)
        else:
            print(letter + suffix)

def find(word,letter,num):
    index = num
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

"""
The following function counts the number of times the letter "a" appears in a string:
word = 'banana'
    count = 0
    for letter in word:
        if letter == 'a':
            count = count + 1
    print(count)
"""
# Encapsulate this function in a function called "count" and generalize so that it 
# accepts the string and the letter as arguments

def count(letterHere, word):
    count = 0
    for letter in word:
        if letter == letterHere:
            count = count + 1
    print(count)

# Rewrite this function so that instead of traversing the string, 
# it uses the three-parameter version of find from the previous section

def count(letterHere,word,num):
    count = 0
    for letter in word:
        i = num
        if letter == letterHere:
            count = count + 1
    print(count)

# the word "in" is a boolean operator that takes two strings and returns "True"
# if the first appears as a substring in the second
# this example prints all the letters from word1 that also appear in word2:

def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)

# check if word is reverse of another
def is_reverse(word1, word2):
    return word1 == reversed(word2)

