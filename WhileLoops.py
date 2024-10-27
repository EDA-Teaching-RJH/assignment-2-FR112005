### Part Two -- your code goes here. 

import random
correct_number = random.randint(1, 100)
user_guess = None

while user_guess != correct_number:
    user_guess = int(input("Guess a number between 1 and 100: "))

    if user_guess > correct_number:
        print("Too high! Try again.")
    elif user_guess < correct_number:
        print("Too low! Try again.")
    else:
        print("Congratulations! You guessed the correct number: {correct_number}")
