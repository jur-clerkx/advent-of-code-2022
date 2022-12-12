def execute_command(line, x, cycle):
    if "noop" in line:
        return x, cycle + 1
    else:
        return x + int(line.split(" ")[1]), cycle + 2


def get_signal_strength(lines):
    x = 1
    cycle = 0
    check = 20
    signal = 0
    for line in lines:
        new_x, new_cycle = execute_command(line, x, cycle)
        if new_cycle >= check:
            signal += x * check
            check += 40
        x, cycle = new_x, new_cycle
    return signal


def print_crt(lines):
    x = 1
    cycle = 0
    line_out = ""
    for line in lines:
        new_x, new_cycle = execute_command(line, x, cycle)
        for i in range(new_cycle - cycle):
            if x - 1 <= cycle <= x + 1:
                line_out += "#"
            else:
                line_out += "."
            cycle += 1
            if len(line_out) == 40:
                print(line_out)
                line_out = ""
                cycle = 0
        x = new_x
    print(line_out)


input_file = open('input/day10.txt', 'r')
input_lines = [line for line in input_file.read().splitlines()]
print(get_signal_strength(input_lines))
print_crt(input_lines)
