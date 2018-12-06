def react_polymer(polymer):
    index = 0
    while index < len(polymer) - 1:
        if (ord(polymer[index]) == ord(polymer[index + 1]) + 32) or (
                ord(polymer[index]) == ord(polymer[index + 1]) - 32):
            del polymer[index]
            del polymer[index]
            index -= 1
            if (index < 0):
                index = 0
        else:
            index += 1
    return polymer


def delete_units(polymer, char):
    if ord(char) < 95:
        char2 = chr(ord(char) + 32)
    else:
        char2 = chr(ord(char) - 32)

    while char in polymer:
        polymer.remove(char)
    while char2 in polymer:
        polymer.remove(char2)
    return polymer


def read_polymer_from_file(file_path):
    polymer = open(file_path, 'r').readline()
    length = len(polymer)
    if polymer[-1] == '\n':
        length -= 1
    return list(polymer[0:length])


def full_react():
    return len(react_polymer(read_polymer_from_file("day05/input.txt")))


def delete_units_and_react():
    length = -1
    for i in range(26):
        polymer = react_polymer(delete_units(read_polymer_from_file("day05/input.txt"), chr(i + 65)))
        if (len(polymer) < length) or (length == -1):
            length = len(polymer)
    return length

