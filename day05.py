from collections import deque


def parse_input(lines):
    stack_lines = []
    command_lines = []
    for line in lines:
        if '[' in line:
            stack_lines.append(line)
        if 'move' in line:
            command_lines.append(line)
    return parse_stack_lines(stack_lines), parse_command_lines(command_lines)


def parse_stack_lines(stack_lines):
    stacks = []
    for i in range((len(stack_lines[0]) + 1) // 4):
        stacks.append(deque())
    for line in stack_lines:
        for i in range(len(stacks)):
            value = line[i * 4 + 1]
            if value != " ":
                stacks[i].appendleft(value)
    return stacks


def parse_command_lines(command_lines):
    commands = []
    for line in command_lines:
        values = line.split(" ")
        commands.append((int(values[1]), int(values[3]), int(values[5])))
    return commands


def execute_commands(stacks, commands):
    for command in commands:
        amount, from_stack, to_stack = command
        for _ in range(amount):
            value = stacks[from_stack - 1].pop()
            stacks[to_stack - 1].append(value)


def execute_new_commands(stacks, commands):
    for command in commands:
        amount, from_stack, to_stack = command
        crates = deque()
        for _ in range(amount):
            crates.append(stacks[from_stack - 1].pop())
        while crates:
            stacks[to_stack - 1].append(crates.pop())


def get_top_values(stacks):
    result = ""
    for stack in stacks:
        result += stack.pop()
    return result


input_file = open('input/day05.txt', 'r')
input_lines = [line for line in input_file.read().splitlines()]
stacks, commands = parse_input(input_lines)
execute_commands(stacks, commands)
print(get_top_values(stacks))
stacks, commands = parse_input(input_lines)
execute_new_commands(stacks, commands)
print(get_top_values(stacks))
