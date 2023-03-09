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
"""

def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True

# c = has_no_e("lame")
# print(c)

"""
Modify your program from the previous section to print only the words
that have no "e" and compute the percentage of words in the list that have no "e". 
"""

fin = open('words.txt')
count = 0
number_words_total = 113809

for line in fin:
    word = line.strip()
    if has_no_e(word) == True:
        count += 1
        print(word)

print(count / number_words_total * 100, '%')

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