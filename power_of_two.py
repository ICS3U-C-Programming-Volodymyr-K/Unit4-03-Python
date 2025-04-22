#!/usr/bin/env python3
# Created By: Volodymyr Kryzhanovskyi
# Date: 04, 15, 2025
# This program  calculates any number to the power fo two.


def main():
    # Gets input for how much times will loop run
    user_loop = input(
        "Enter the number ranging from 0 to what number you want to get squared."
    )
    # Catches any input from user besides integer
    try:
        user_loop = int(user_loop)
        # Displays that user input can't be negative if it is negative
        if user_loop < 0:
            print("Your integer should be positive.")
            # For loop calculating each number to the power of 2 till the loop set by the user ends
        for counter in range(user_loop + 1):
            power = counter**2
            print(f"{counter}**2 = {power}")
            # Displays the sentence below if users enters anything besides integer
    except Exception:
        print("Number should be integer.")


if __name__ == "__main__":
    main()
