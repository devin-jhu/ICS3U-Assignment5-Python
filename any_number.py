#!/usr/bin/env python3

# Created by Devin Jhu
# Created on May 2022
# The loop multiplier


def main():
    # this program shows the string of number entered
    HI = 1
    counter = 1
    hello_number = HI

    # input
    number = input("Enter number (integer): ")

    # process & output
    try:
        number_int = int(number)
        if number_int <= 0:
            print("Not a positive number")
        else:
            for counter in range(number_int):
                hello_number = HI + counter
                print("HI", end="")
    except Exception:
        print("Not a number.")
    print("\nDone.")


if __name__ == "__main__":
    main()
