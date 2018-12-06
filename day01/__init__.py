#!/usr/bin/python3

def read_file():
    return open("day01/input.txt", 'r')


def count_frequency():
    result = 0
    file = read_file()
    for line in file:
        number = int(line[1:])
        if line[0] == '+':
            result += number
        elif line[0] == '-':
            result -= number
    file.close()
    return result


def found_twice_frequency():
    array_of_results = [0]
    result = 0

    file = read_file()
    for line in file:
        number = int(line[1:])
        if line[0] == '+':
            result += number
        elif line[0] == '-':
            result -= number
        if result in array_of_results:
            file.close()
            return result
        array_of_results.append(result)
        array_of_results.sort()
    file.close()

    while True:
        file = read_file()
        for line in file:
            number = int(line[1:])
            if line[0] == '+':
                result += number
            elif line[0] == '-':
                result -= number
            if result in array_of_results:
                file.close()
                return result
        file.close()

