def is_fully_containing(start1, end1, start2, end2):
    return (start1 <= start2 and end1 >= end2) or (start2 <= start1 and end2 >= end1)


def parse_line(line):
    pairs = line.split(',')
    pair1 = pairs[0].split('-')
    pair2 = pairs[1].split('-')
    return int(pair1[0]), int(pair1[1]), int(pair2[0]), int(pair2[1])


def get_fully_containing_pair_count(lines):
    result = 0
    for line in lines:
        start1, end1, start2, end2 = parse_line(line)
        if is_fully_containing(start1, end1, start2, end2):
            result += 1
    return result


def is_overlapping(start1, end1, start2, end2):
    return (start2 <= start1 <= end2) or (start2 <= end1 <= end2) or (start1 <= start2 <= end1) or \
           (start1 <= end2 <= end1)


def get_overlapping_pair_count(lines):
    result = 0
    for line in lines:
        start1, end1, start2, end2 = parse_line(line)
        if is_overlapping(start1, end1, start2, end2):
            result += 1
    return result


input_file = open('input/day04.txt', 'r')
input_lines = [line for line in input_file.read().splitlines()]
print(get_fully_containing_pair_count(input_lines))
print(get_overlapping_pair_count(input_lines))
