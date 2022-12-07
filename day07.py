class File:
    def __init__(self, name: str, parent: 'Folder', size: int) -> None:
        self.name = name
        self.size = size
        self.parent = parent

    def get_size(self):
        return self.size


class Folder:
    def __init__(self, name: str, parent: 'Folder') -> None:
        self.name = name
        self.parent = parent
        self.children = []
        super().__init__()

    def get_size(self) -> int:
        size = 0
        for child in self.children:
            size += child.get_size()
        return size


class State:
    pass


State.outer_folder = Folder('/', parent=None)

State.folders = []
State.current_folder = None


def parse_file_or_folder(line):
    arguments = line.split(" ")
    if arguments[0] == "dir":
        folder = Folder(arguments[1], State.current_folder)
        State.current_folder.children.append(folder)
        State.folders.append(folder)
    else:
        file = File(arguments[1], State.current_folder, int(arguments[0]))
        State.current_folder.children.append(file)


def process_cd_command(line):
    argument = line.split(" ")[2]
    if argument == "/":
        State.current_folder = State.outer_folder
    if argument == "..":
        State.current_folder = State.current_folder.parent
    else:
        for child in State.current_folder.children:
            if child.name == argument:
                State.current_folder = child
                break


def process_inputs(lines):
    listing = False
    for line in lines:
        if listing:
            if '$' in line:
                listing = False
            else:
                parse_file_or_folder(line)
                continue
        if '$ cd' in line:
            process_cd_command(line)
        if '$ ls' in line:
            listing = True


def total_folder_count(max_size: int) -> int:
    total = 0
    for folder in State.folders:
        if folder.get_size() <= max_size:
            total += folder.get_size()
    return total


def find_smallest_folder_size(min_size: int) -> int:
    lowest = State.outer_folder.get_size()
    for folder in State.folders:
        if min_size <= folder.get_size() < lowest:
            lowest = folder.get_size()
    return lowest


input_file = open('input/day07.txt', 'r')
input_lines = [line for line in input_file.read().splitlines()]
process_inputs(input_lines)
print(total_folder_count(100_000))
needed_space = 30_000_000
total_space = 70_000_000
free_space = total_space - State.outer_folder.get_size()
print(find_smallest_folder_size(needed_space - free_space))
