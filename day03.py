def get_total_line_priority(lines):
    result = 0
    for line in lines:
        result += get_line_priority(line)
    return result


def get_line_priority(line):
    first_half, second_half = line[:len(line) // 2], line[len(line) // 2:]
    unique_char = list(set(first_half) & set(second_half))[0]
    value = ord(unique_char)
    return char_priority(value)


def get_total_group_priorities(lines):
    result = 0
    for i in range(0, len(lines), 3):
        unique_char = list(set(set(lines[i]) & set(lines[i + 1]) & set(lines[i + 2])))[0]
        result += char_priority(ord(unique_char))
    return result


def char_priority(char):
    if 97 <= char <= 122:
        return char - 96
    if 65 <= char <= 90:
        return char - 38


input_file = open('input/day03.txt', 'r')
input = [line for line in input_file.read().splitlines()]
print(get_total_line_priority(input))
print(get_total_group_priorities(input))
