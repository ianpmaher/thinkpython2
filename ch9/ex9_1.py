"""
Write a program that reads words.txt and prints only the words with more than 20 characters
excluding whitespaces.
"""

def bigwords():
    fin = open('words.txt')
    for line in fin:
        words = line.strip()
        if len(words) > 20:
            print(words)

"""
Write a function called has_no_e that returns True if the given word
doesn't have the letter "e" in it.
Modify your program from the previous section to print only the words
that have no "e" and compute the percentage of words in the list that have no "e". 
"""

def has_no_e():
    fin = open('words.txt')
    for line in fin:
        words = line.strip()
        