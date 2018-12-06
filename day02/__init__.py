#!/usr/bin/python3

def read_file():
    return open("day02/input.txt")


def sums():
    file = read_file()
    count2 = 0
    count3 = 0
    for line in file:
        count_chars = [0] * 26
        for i in range(26):
            char = chr(97 + i)
            count_char = 0
            for j in range(len(line)):
                if char == line[j]:
                    count_char += 1
            count_chars[i] = count_char

        if 2 in count_chars:
            count2 += 1
        if 3 in count_chars:
            count3 += 1
    return count2 * count3


def find_correct_boxes():
    lines = read_file().readlines()
    length = len(lines[0])
    result = ""
    for line1 in range(len(lines) - 1):
        for line2 in range(line1 + 1, len(lines)):
            result_new = ""
            for i in range(length):
                if (lines[line1][i] == lines[line2][i]) and lines[line1][i] != '\n':
                    result_new += lines[line1][i]
            if len(result_new) > len(result):
                result = result_new
    return result

