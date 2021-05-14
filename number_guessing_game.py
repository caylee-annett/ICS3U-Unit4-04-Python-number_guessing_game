#!/usr/bin/env python3

# Created by: Caylee Annett
# Created on: May 2021
# This program is a game where the user tries to guess a randomly
#   generated number and uses a break statement


import random


def main():
    # This function tells the user if their guess is correct

    # Input
    guess_as_string = input("Guess what the integer between 0 and 10 is: ")
    print("")

    # Process & Output
    correct_number = random.randint(0, 10)
    while True:
        try:
            guess_as_integer = int(guess_as_string)

            if guess_as_integer == correct_number:
                print("You guessed it!")
                break
            elif guess_as_integer > correct_number:
                print("Incorrect! {} is too high.".format(
                    guess_as_integer))
                print("")
            else:
                print("Incorrect! {} is too low.".format(
                    guess_as_integer))
                print("")
        except Exception:
            print("{} is not a valid input.".format(
                guess_as_string))
            print("")
        guess_as_string = input("Try again: ")
    print("\nDone.")


if __name__ == "__main__":
    main()
