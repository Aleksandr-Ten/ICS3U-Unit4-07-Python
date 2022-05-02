#!/usr/bin/env python3

# Created by: Aleksandr Ten
# Created on: April 2022
# This program calculates numbers from 1000 to 2000


def main():
    # this function is a loop
    loop_counter = 1000
    end_number = 2000

    # process & output
    for loop_counter in range(loop_counter, end_number + 1):
        if loop_counter % 5 == 4:
            print("{0} ".format(loop_counter))
        else:
            print("{0} ".format(loop_counter), end="")
    print("\n\nDone.")


if __name__ == "__main__":
    main()
