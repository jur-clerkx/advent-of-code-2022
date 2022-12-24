class Shape:

    def __init__(self, positions: list[tuple[int, int]]) -> None:
        super().__init__()
        self.positions = positions

    def move_right(self, state: set[tuple[int, int]]):
        new_positions = []
        for x, y in self.positions:
            new_positions.append((x + 1, y))
            if x + 1 > 6 or (x + 1, y) in state:
                return
        self.positions = new_positions

    def move_left(self, state: set[tuple[int, int]]):
        new_positions = []
        for x, y in self.positions:
            new_positions.append((x - 1, y))
            if x - 1 < 0 or (x - 1, y) in state:
                return
        self.positions = new_positions

    def move_down(self, state: set[tuple[int, int]]) -> bool:
        new_positions = []
        for x, y in self.positions:
            new_positions.append((x, y - 1))
            if y - 1 < 0 or (x, y - 1) in state:
                return False
        self.positions = new_positions
        return True

    def get_highest_position(self):
        result = 0
        for _, y in self.positions:
            if y > result:
                result = y
        return result


def generate_horizontal_line(highest: int) -> Shape:
    return Shape([(2, highest + 4), (3, highest + 4), (4, highest + 4), (5, highest + 4)])


def generate_plus(highest: int) -> Shape:
    return Shape([(2, highest + 5), (3, highest + 5), (4, highest + 5), (3, highest + 4), (3, highest + 6)])


def generate_l(highest: int) -> Shape:
    return Shape([(2, highest + 4), (3, highest + 4), (4, highest + 4), (4, highest + 5), (4, highest + 6)])


def generate_vertical_line(highest: int) -> Shape:
    return Shape([(2, highest + 4), (2, highest + 5), (2, highest + 6), (2, highest + 7)])


def generate_block(highest: int) -> Shape:
    return Shape([(2, highest + 4), (3, highest + 4), (2, highest + 5), (3, highest + 5)])


generators = [generate_horizontal_line, generate_plus, generate_l, generate_vertical_line, generate_block]


def drop_rocks(amount: int, generators: list, jets: str) -> set[tuple[int, int]]:
    state = set()
    highest = -1
    generator_index = 0
    generator_len = len(generators)
    jet_index = 0
    jet_len = len(jets)
    for i in range(amount):
        if i % 1_000_000 == 0:
            print(i)
        shape = generators[generator_index % generator_len](highest)
        generator_index += 1
        drop = True
        while drop:
            jet = jets[jet_index % jet_len]
            jet_index += 1
            if jet == "<":
                shape.move_left(state)
            if jet == ">":
                shape.move_right(state)
            drop = shape.move_down(state)
        if highest < shape.get_highest_position():
            highest = shape.get_highest_position()
        for position in shape.positions:
            state.add(position)
    return highest + 1


input_file = open('input/day17.txt', 'r')
jets = [line for line in input_file.read().splitlines()][0]
print(drop_rocks(2022, generators, jets))
print(drop_rocks(1_000_000_000_000, generators, jets))
