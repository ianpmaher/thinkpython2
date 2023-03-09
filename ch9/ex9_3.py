"""
Write a function named avoids that takes a word and a string of forbidden letters, and 
that returns True if the word doesn't use any of the forbidden letters.
"""
"""
Modify your program to prompt the user to enter a string of forbidden letters and 
then print the number of words that don't contain any of them. Can you find a
combo of five forbidden letters that excludes the smallest number of words?
"""

def avoids(word, string):
    for char in string:
        if char in word:
            return False
    return True

fin = open("words.txt")

forbidden=input("Enter the forbidden characters: ")  
fin=open("words.txt")  

def avoids_forbidden():    
    for letter in fin:    # Searches the letter in the file
        word=letter.strip()    
        if forbidden not in word:    #If forbidden char is not in the file
            print(word)    
print(avoids_forbidden())  