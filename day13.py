import functools


def parse_pairs(lines):
    result = []
    for i in range(0, len(lines), 3):
        left = eval(lines[i])
        right = eval(lines[i + 1])
        result.append((left, right))
    return result


def parse_lines(lines):
    result = []
    for line in lines:
        if line:
            result.append(eval(line))
    return result


def compare_integers(left: int, right: int) -> int:
    if left == right:
        return 0
    if left < right:
        return 1
    return -1


def compare_lists(left: list, right: list) -> int:
    for i in range(len(left)):
        if len(right) - 1 < i:
            return -1
        result = compare(left[i], right[i])
        if abs(result) == 1:
            return result
    if len(left) == len(right):
        return 0
    else:
        return 1


def compare(left, right) -> int:
    if isinstance(left, int) and isinstance(right, int):
        return compare_integers(left, right)
    if isinstance(left, list) and isinstance(right, list):
        return compare_lists(left, right)
    if isinstance(left, int) and isinstance(right, list):
        return compare_lists([left], right)
    if isinstance(left, list) and isinstance(right, int):
        return compare_lists(left, [right])
    return 0


input_file = open('input/day13.txt', 'r')
input_lines = [line for line in input_file.read().splitlines()]
pairs = parse_pairs(input_lines)

result = 0
for i in range(len(pairs)):
    left, right = pairs[i]
    if compare(left, right) == 1:
        result += i + 1
print(result)

lines = parse_lines(input_lines)
lines.append([[2]])
lines.append([[6]])
lines.sort(key=functools.cmp_to_key(compare), reverse=True)
index1 = 0
index2 = 0
for i in range(len(lines)):
    if lines[i] == [[2]]:
        index1 = i + 1
    if lines[i] == [[6]]:
        index2 = i + 1
print(index1 * index2)
