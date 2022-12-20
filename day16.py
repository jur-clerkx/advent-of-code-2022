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


def find_shortest_path(start: Valve, end: Valve, valves: dict[str, Valve]) -> int:
    queue = [(start, 0)]
    visited = set()

    while queue:
        current_valve, steps = queue.pop(0)
        if current_valve == end:
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
