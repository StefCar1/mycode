#!/usr/bin/env python3
"""Number guessing game! User has 5 chances to guess a number between 1 and 100!"""

import random

def main():
    num = random.randint(1, 100)  # Generate the random number
    rounds = 0  # Initialize the round counter

    while rounds < 5:  # The loop should only track rounds
        guess = input("Guess a number between 1 and 100\n> ")

        # COOL CODE ALERT: The next lines check if the input is a valid digit
        # If not, it skips the loop iteration and asks again
        if guess.isdigit():
            guess = int(guess)  # Convert input to integer
        else:
            print("Invalid input, please enter a valid number.")
            continue  # Skip to the next loop iteration if input is not a number

        if guess > num:
            print("Too high!")
        elif guess < num:
            print("Too low!")
        else:
            print("Correct! You guessed the number!")
            break  # Exit the loop if the guess is correct

        rounds += 1  # Increment the round counter

    if rounds == 5 and guess != num:  # If the player fails to guess within 5 attempts
        print(f"Out of attempts! The correct number was {num}.")

if __name__ == "__main__":
    main()
