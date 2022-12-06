from collections import deque


def get_first_packet(line, size):
    queue = deque()
    charcounter = 0
    for char in line:
        queue.append(char)
        charcounter += 1
        if len(queue) > size:
            queue.popleft()
        if len(queue) == size:
            if len(set(queue)) == size:
                return charcounter


input_file = open('input/day06.txt', 'r')
input_line = input_file.read()
print(get_first_packet(input_line, 4))
print(get_first_packet(input_line, 14))
