#!/usr/bin/python3
from day01 import count_frequency, found_twice_frequency
from day05 import full_react, delete_units_and_react


def main():
    #day01
    print('01a - ' + str(count_frequency()))
    print('01b - ' + str(found_twice_frequency()))
    # day05a
    print('05a - ' + str(full_react()))
    print('05b - ' + str(delete_units_and_react()))
    return


main()
