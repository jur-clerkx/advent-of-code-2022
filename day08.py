def parse_input(lines):
    grid = []
    for line in lines:
        xline = []
        grid.append(xline)
        for char in line:
            xline.append(int(char))
    return grid


def check_x_range(x_range, y, grid, current_tree):
    for x in x_range:
        if grid[y][x] >= current_tree:
            return False
    return True


def check_y_range(x, y_range, grid, current_tree):
    for y in y_range:
        if grid[y][x] >= current_tree:
            return False
    return True


def check_visibility(x, y, x_max, y_max, grid):
    tree_height = grid[y][x]
    if check_x_range(range(0, x), y, grid, tree_height) or \
            check_x_range(range(x + 1, x_max + 1), y, grid, tree_height) or \
            check_y_range(x, range(0, y), grid, tree_height) or \
            check_y_range(x, range(y + 1, y_max + 1), grid, tree_height):
        return True
    return False


def is_visible(x, y, x_max, y_max, grid):
    if x == 0 or y == 0 or x == x_max or y == y_max:
        return 1
    if check_visibility(x, y, x_max, y_max, grid):
        return 1
    return 0


def get_visibility_count(grid):
    y_max = len(grid)
    x_max = len(grid[0])
    result = 0
    for y in range(y_max):
        for x in range(x_max):
            result += is_visible(x, y, x_max - 1, y_max - 1, grid)
    return result


def get_score(x, y, x_range, y_range, grid):
    current = grid[y][x]
    count = 0
    for y_check in y_range:
        for x_check in x_range:
            count += 1
            if grid[y_check][x_check] >= current:
                return count
    return count


def scenic_score(x, y, x_max, y_max, grid):
    return get_score(x, y, reversed(range(0, x)), range(y, y + 1), grid) * \
        get_score(x, y, range(x + 1, x_max), range(y, y + 1), grid) * \
        get_score(x, y, range(x, x + 1), reversed(range(0, y)), grid) * \
        get_score(x, y, range(x, x + 1), range(y + 1, y_max), grid)


def get_highest_scenic_score(grid):
    highest = 0
    x_max = len(grid[0])
    y_max = len(grid)
    for y in range(y_max):
        for x in range(x_max):
            score = scenic_score(x, y, x_max, y_max, grid)
            if score > highest:
                highest = score
    return highest


input_file = open('input/day08.txt', 'r')
input_lines = [line for line in input_file.read().splitlines()]
grid = parse_input(input_lines)
print(get_visibility_count(grid))
print(get_highest_scenic_score(grid))
