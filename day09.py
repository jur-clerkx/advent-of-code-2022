def do_command(command, head_x, head_y):
    if command == "R":
        return head_x + 1, head_y
    if command == "L":
        return head_x - 1, head_y
    if command == "U":
        return head_x, head_y + 1
    if command == "D":
        return head_x, head_y - 1


def translate_tail(head_x, head_y, tail_x, tail_y):
    dif_x = head_x - tail_x
    dif_y = head_y - tail_y
    result_x, result_y = tail_x, tail_y
    if abs(dif_x) == 2:
        result_x = tail_x + dif_x / 2
        if dif_y != 0:
            result_y = tail_y + dif_y
    if abs(dif_y) == 2:
        result_y = tail_y + dif_y / 2
        if dif_x != 0:
            result_x = tail_x + dif_x
    return result_x, result_y


def get_tail_visited_count(commands, rope_length):
    head_x, head_y = 0, 0
    tails = []
    for _ in range(rope_length - 1):
        tails.append((0, 0))
    tail_visited = set()
    for command in commands:
        head_x, head_y = do_command(command, head_x, head_y)
        for i in range(rope_length - 1):
            if i == 0:
                tail_x, tail_y = tails[i]
                tails[i] = translate_tail(head_x, head_y, tail_x, tail_y)
                if rope_length == 2:
                    tail_visited.add(tails[i])
                continue
            follow_x, follow_y = tails[i - 1]
            tail_x, tail_y = tails[i]
            tails[i] = translate_tail(follow_x, follow_y, tail_x, tail_y)
            if i == rope_length - 2:
                tail_visited.add(tails[i])
    return len(tail_visited)


def parse_input(lines):
    commands = []
    for line in lines:
        args = line.split(" ")
        for _ in range(int(args[1])):
            commands.append(args[0])
    return commands


input_file = open('input/day09.txt', 'r')
input_lines = [line for line in input_file.read().splitlines()]
commands = parse_input(input_lines)
print(get_tail_visited_count(commands, 10))
