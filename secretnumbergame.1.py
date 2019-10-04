#!/usr/bin/env python3

# Created by: Douglass Jeffrey
# Created on: Oct 2019
# This program plays a number generation game


import constants


def main():
    # this function checks user inputted number is the same as the computers
    # secret number

    # input
    user_number = int(input("Enter your number: "))
    print("")

    # process & output
    if user_number == constants.SECRETNUMBER:
        print("You got the answer right!!!")
    else:
        print("You got the answer wrong, try again.")


if __name__ == "__main__":
    main()
