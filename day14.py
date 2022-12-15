def generate_line(start, end, grid):
    grid[start] = "#"
    grid[end] = "#"
    start_x, start_y = start
    end_x, end_y = end
    if start_x != end_x:
        dif_x = end_x - start_x
        for x in range(start_x, end_x, dif_x // abs(dif_x)):
            grid[(x, start_y)] = "#"
    if start_y != end_y:
        dif_y = end_y - start_y
        for y in range(start_y, end_y, dif_y // abs(dif_y)):
            grid[(start_x, y)] = "#"


def parse_pairs(pairs, grid):
    parsed = []
    for pair in pairs:
        parts = pair.split(",")
        parsed.append((int(parts[0]), int(parts[1])))
    for i in range(len(parsed) - 1):
        generate_line(parsed[i], parsed[i + 1], grid)


def parse_input(lines):
    result = {}
    for line in lines:
        pairs = line.split(" -> ")
        parse_pairs(pairs, result)
    return result


def get_lowest(grid):
    lowest = 0
    for _, y in grid:
        if y > lowest:
            lowest = y
    return lowest


def get_rest_position(start, grid, lowest, limit):
    x, y = start
    while (True):
        if y >= lowest and not limit:
            return None
        if y == lowest + 1 and limit:
            return x, y
        if grid.get((x, y + 1)) is None:
            y = y + 1
            continue
        elif grid.get((x - 1, y + 1)) is None:
            x = x - 1
            y = y + 1
            continue
        elif grid.get((x + 1, y + 1)) is None:
            x = x + 1
            y = y + 1
            continue
        else:
            return x, y


def fill_grid_with_sand(grid, limit):
    lowest = get_lowest(grid)
    count = 0
    while True:
        pos = get_rest_position((500, 0), grid, lowest, limit)
        if not pos:
            return count
        grid[pos] = "o"
        count += 1
        if pos == (500, 0):
            return count


input_file = open('input/day14.txt', 'r')
input_lines = [line for line in input_file.read().splitlines()]

grid = parse_input(input_lines)
print(fill_grid_with_sand(grid, False))

grid = parse_input(input_lines)
print(fill_grid_with_sand(grid, True))

