#!/usr/bin/env python3

# Created by Devin Jhu
# Created on May 2022
# The loop string


def main():
    # this program shows the string of number entered
    counter = 1

    # input
    number = input("Enter number (integer): ")
    string = input("Enter string: ")
    # process & output
    try:
        number_int = int(number)
        if number_int <= 0:
            print("Not a positive number")
        else:
            for counter in range(number_int):
                print("{0}".format(string), end="")
    except Exception:
        print("Not a number.")
    print("\nDone.")


if __name__ == "__main__":
    main()
