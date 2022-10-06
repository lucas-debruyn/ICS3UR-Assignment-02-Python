#!/usr/bin/env python3

# Created by: Lucas DeBruyn
# Created on: Oct 2022
# This program calculates the perimeter of a pentagon
#    with sides inputted from the user


def main():
    # this function calculates perimeter

    # input
    length_one = int(input("Enter length of the first side of the pentagon (cm): "))
    length_two = int(input("Enter length of the second side of the pentagon (cm): "))
    length_three = int(input("Enter length of the third side of the pentagon (cm): "))
    length_four = int(input("Enter length of the fourth side of the pentagon (cm): "))
    length_five = int(input("Enter length of the fifth side of the pentagon (cm): "))

    # process
    perimeter = length_one + length_two + length_three + length_four + length_five

    # output
    print("")
    print("Perimeter is {0} cm.".format(perimeter))

    print("\nDone.")


if __name__ == "__main__":
    main()
