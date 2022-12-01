def parse_input(input):
    result = []
    current = 0
    for line in input:
        if line:
            current += int(line)
        else:
            result.append(current)
            current = 0
    result.sort(reverse=True)
    return result


def get_highest_calory_count(input):
    return input[0]


def get_highest_three_calory_count(input):
    return input[0] + input[1] + input[2]


input_file = open('input/day01.txt', 'r')
input = [line for line in input_file.read().splitlines()]
input = parse_input(input)
print(get_highest_calory_count(input))
print(get_highest_three_calory_count(input))
