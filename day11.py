import operator
import math

ops = {
    "+": operator.add,
    "*": operator.mul,
}


class Monkey:

    def __init__(self) -> None:
        self.processing = 0

    def inspect_items(self, monkeys, lcm):
        for number in self.items:
            result = number
            if self.operator_input == "old":
                result = self.operator(result, result)
            else:
                result = self.operator(result, int(self.operator_input))
            # result = int(result / 3)
            result = result % lcm
            if result % self.dividable == 0:
                monkeys[self.true_index].items.append(result)
            else:
                monkeys[self.false_index].items.append(result)
        self.processing += len(self.items)
        self.items = []


def parse_input(lines):
    monkeys = []
    current_monkey = None
    for line in lines:
        if "Monkey" in line:
            current_monkey = Monkey()
            monkeys.append(current_monkey)
        if "Starting items:" in line:
            string_numbers = line[18:].split(",")
            numbers = []
            for string_number in string_numbers:
                numbers.append(int(string_number.strip()))
            current_monkey.items = numbers
        if "Operation:" in line:
            current_monkey.operator = ops.get(line[23:24])
            current_monkey.operator_input = line[25:]
        if "Test:" in line:
            current_monkey.dividable = int(line[21:])
        if "If true" in line:
            current_monkey.true_index = int(line[29:30])
        if "If false" in line:
            current_monkey.false_index = int(line[30:31])
    return monkeys


def do_rounds(rounds, monkeys, lcm):
    for i in range(rounds):
        for monkey in monkeys:
            monkey.inspect_items(monkeys, lcm)


def monkey_lcm(monkeys):
    divisions = []
    for monkey in monkeys:
        divisions.append(monkey.dividable)
    return math.lcm(*divisions)


input_file = open('input/day11.txt', 'r')
input_lines = [line for line in input_file.read().splitlines()]
monkeys = parse_input(input_lines)
do_rounds(10_000, monkeys, monkey_lcm(monkeys))
for monkey in monkeys:
    print(monkey.processing)
