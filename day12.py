import sys

sys.setrecursionlimit(20000)


class Field:
    def __init__(self, height: int, x: int, y: int) -> None:
        self.height = height
        self.position = (x, y)
        self.turns = -1

    def check_move(self, other_height, turn, positions) -> None:
        if other_height + 1 < self.height:
            return
        if turn + 1 < self.turns or self.turns == -1:
            self.turns = turn + 1
            surrounding = self.get_surrounding(positions)
            for field in surrounding:
                field.check_move(self.height, self.turns, positions)

    def add_surrounding(self, position, result):
        if position:
            result.append(position)

    def get_surrounding(self, positions):
        results = []
        x, y = self.position
        self.add_surrounding(positions.get((x + 1, y)), results)
        self.add_surrounding(positions.get((x - 1, y)), results)
        self.add_surrounding(positions.get((x, y + 1)), results)
        self.add_surrounding(positions.get((x, y - 1)), results)
        return results


def parse_input(lines) -> (Field, Field, dict):
    start = None
    end = None
    positions = {}
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            val = lines[y][x]
            if val == 'S':
                start = Field(0, x, y)
                positions[(x, y)] = start
            elif val == 'E':
                end = Field(27, x, y)
                positions[(x, y)] = end
            else:
                positions[(x, y)] = Field(ord(val) - 96, x, y)
    return start, end, positions


def check_surrounding(x, y, positions):
    start_field = positions[(x, y)]
    surrounding = start_field.get_surrounding(positions)
    for field in surrounding:
        field.check_move(start.height, 0, positions)


def get_lowest_indexes(start, positions):
    results = [start.position]
    for i in positions:
        field = positions[i]
        if field.height == 1:
            results.append(field.position)
    return results


input_file = open('input/day12.txt', 'r')
input_lines = [line for line in input_file.read().splitlines()]
start, end, positions = parse_input(input_lines)
x, y = start.position
check_surrounding(x, y, positions)
print(end.turns)

start, end, positions = parse_input(input_lines)
lowest_starting_points = get_lowest_indexes(start, positions)
print(len(lowest_starting_points))
lowest = 1000000
for point in lowest_starting_points:
    print("run")
    start, end, positions = parse_input(input_lines)
    x, y = point
    check_surrounding(x, y, positions)
    if end.turns < lowest and end.turns != -1:
        lowest = end.turns
print(lowest)
