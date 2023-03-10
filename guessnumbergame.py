# guess.py

from random import randint

secret = randint(1, 10)

print("Welcome, friend!")

name = ""
while not name:
    name = input("Enter your name: ").strip()

while True:
    user_input = input("Guess a number between 1 and 10: ")
    if not user_input.isdigit():
        user_input = input("Please enter a valid number: ")
    guess = int(user_input)
    if guess == secret:
        print(f"Congrats {name}! You win!")
        break
    elif guess > secret:
        print("The secret number is lower than your guess...")
    else:
        print("The secret number is greater than your guess...")