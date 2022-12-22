import re


class Valve:
    def __init__(self, name: str, rate: int, neighbours: set) -> None:
        super().__init__()
        self.name = name
        self.rate = rate
        self.neighbours = neighbours
        self.released = False

    def get_max_pressure_release(self, from_valve: str, valves: dict[str, 'Valve'], remaining_steps: int) -> (int, int):
        if self.released or self.rate == 0:
            return 0, 0
        effort = find_shortest_path(valves[from_valve], self, valves) + 1
        max_pressure_release = (remaining_steps - effort) * self.rate
        return max_pressure_release, effort


path_cache = dict()


def find_shortest_path(start: Valve, end: Valve, valves: dict[str, Valve]) -> int:
    queue = [(start, 0)]
    visited = set()

    if path_cache.get((start.name, end.name)):
        return path_cache.get((start.name, end.name))

    while queue:
        current_valve, steps = queue.pop(0)
        if current_valve == end:
            path_cache[(start.name, end.name)] = steps
            path_cache[(end.name, start.name)] = steps
            return steps
        if current_valve not in visited:
            visited.add(current_valve)
            for neighbour in current_valve.neighbours:
                queue.append((valves[neighbour], steps + 1))
    return -1


def get_all_possible_releases(path: list, valves: dict[str, Valve], steps, current_score):
    current = path[-1]
    highest_score = current_score
    for valve in valves:
        valve = valves[valve]
        if valve.name not in path:
            score, effort = valve.get_max_pressure_release(current, valves, steps)
            if score > 0 and effort <= steps:
                new_path = path.copy()
                new_path.append(valve.name)
                path_score = get_all_possible_releases(new_path, valves, steps - effort, current_score + score)
                if path_score > highest_score:
                    highest_score = path_score
    return highest_score


def get_all_possible_releases_for_two(path1: list, path2: list, valves: dict[str, Valve], steps1, steps2,
                                      current_score):
    current1 = path1[-1]
    current2 = path2[-1]
    highest_score = current_score
    # Action for 1
    for valve in valves:
        valve = valves[valve]
        if valve.name not in path1 and valve.name not in path2:
            score, effort = valve.get_max_pressure_release(current1, valves, steps1)
            if score > 0 and effort <= steps1:
                new_path = path1.copy()
                new_path.append(valve.name)
                path_score = get_all_possible_releases_for_two(new_path, path2, valves, steps1 - effort, steps2,
                                                               current_score + score)
                if path_score > highest_score:
                    highest_score = path_score
    # Action for 2
    for valve in valves:
        valve = valves[valve]
        if valve.name not in path1 and valve.name not in path2:
            score, effort = valve.get_max_pressure_release(current2, valves, steps2)
            if score > 0 and effort <= steps1:
                new_path = path2.copy()
                new_path.append(valve.name)
                path_score = get_all_possible_releases_for_two(path1, new_path, valves, steps1, steps2 - effort,
                                                               current_score + score)
                if path_score > highest_score:
                    highest_score = path_score
    return highest_score


def parse_input(lines: list[str]) -> dict[str, Valve]:
    result = {}
    for line in lines:
        flow_rate = int(re.findall(r'rate=(-?\d+);', line)[0])
        names = re.findall(r'[A-Z]{2}', line)
        valve = Valve(names[0], flow_rate, set(names[1:]))
        result[valve.name] = valve
    return result


input_file = open('input/day16.txt', 'r')
input_lines = [line for line in input_file.read().splitlines()]
valves = parse_input(input_lines)
print(get_all_possible_releases(["AA"], valves, 30, 0))

print(get_all_possible_releases_for_two(["AA"], ["AA"], valves, 26, 26, 0))
