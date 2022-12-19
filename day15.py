import re


def parse_input(lines: list) -> list:
    result = []
    for line in lines:
        coords = re.findall(r'x=(-?\d+), y=(-?\d+)', line)
        x1, y1 = map(int, coords[0])
        x2, y2 = map(int, coords[1])
        result.append((x1, y1, x2, y2))
    return result


def get_sensor_coverage_for_y_row(sensors: list, y_row: int) -> set:
    result = set()
    for x1, y1, x2, y2 in sensors:
        signal_distance = abs(x1 - x2) + abs(y1 - y2)
        x_rest = signal_distance - abs(y_row - y1)
        if x_rest >= 0:
            for x in range(x1 - x_rest, x1 + x_rest + 1, 1):
                result.add(x)
    return result


def get_beacon_positions_for_y_row(sensors: list, y_row: int) -> set:
    result = set()
    for x1, y1, x2, y2 in sensors:
        if y2 == y_row:
            result.add(x2)
    return result


def get_coverage_count_for_y_row(sensors: list, y_row: int) -> int:
    return len(get_sensor_coverage_for_y_row(sensors, y_row) - get_beacon_positions_for_y_row(sensors, y_row))


def get_all_border_positions(sensors: list, x_min: int, x_max: int, y_min: int, y_max: int) -> set:
    result = set()
    for x1, y1, x2, y2 in sensors:
        border_distance = abs(x1 - x2) + abs(y1 - y2) + 1
        for x in range(x1 - border_distance, x1 + border_distance + 1, 1):
            if x_min <= x <= x_max:
                y_distance = border_distance - abs(x - x1)
                y_top = y1 + y_distance
                y_bottom = y1 - y_distance
                if y_min <= y_top <= y_max:
                    result.add((x, y_top))
                if y_min <= y_bottom <= y_max:
                    result.add((x, y_bottom))
    return result


def get_free_beacon_position(border_positions: set, sensors: list) -> tuple:
    for x, y in border_positions:
        found = False
        if x == 14 and y == 11:
            pass
        for x1, y1, x2, y2 in sensors:
            sensor_range = abs(x1 - x2) + abs(y1 - y2)
            distance_to_sensor = abs(x - x1) + abs(y - y1)
            if distance_to_sensor <= sensor_range:
                found = True
                break
        if not found:
            return x, y


input_file = open('input/day15.txt', 'r')
input_lines = [line for line in input_file.read().splitlines()]
sensors = parse_input(input_lines)

print(get_coverage_count_for_y_row(sensors, 2000000))
x, y = get_free_beacon_position(get_all_border_positions(sensors, 0, 4000000, 0, 4000000), sensors)
print(x*4000000 + y)
