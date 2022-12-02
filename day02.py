from enum import IntEnum


class PlayType(IntEnum):
    ROCK_LOSE = 1
    PAPER_DRAW = 2
    SCISSORS_WIN = 3


def parse_play_type(input):
    if input == "A" or input == "X":
        return PlayType.ROCK_LOSE
    if input == "B" or input == "Y":
        return PlayType.PAPER_DRAW
    if input == "C" or input == "Z":
        return PlayType.SCISSORS_WIN


def parse_input(input):
    result = []
    for line in input:
        play = line.split(' ')
        result.append((parse_play_type(play[0]), parse_play_type(play[1])))
    return result


def calculate_winner(play):
    player1, player2 = play
    return (3 + player1 - player2) % 3


def calculate_strategy_points(plays):
    result = 0
    for play in plays:
        _, my_move = play
        result += my_move
        winner = calculate_winner(play)
        if winner == 0:  # Draw
            result += 3
        if winner == 2:
            result += 6
    return result


def implement_strategy_guide(plays):
    result = 0
    for play in plays:
        op_move, my_move = play
        if my_move == PlayType.PAPER_DRAW:
            result += 3
            result += op_move
        if my_move == PlayType.ROCK_LOSE:
            move = op_move - 1
            if move < 1:
                move = move + 3
            result += move
        if my_move == PlayType.SCISSORS_WIN:
            result += 6
            move = (op_move + 1)
            if move > 3:
                move = move - 3
            result += move
    return result


input_file = open('input/day02.txt', 'r')
input = [line for line in input_file.read().splitlines()]
input = parse_input(input)
print(calculate_strategy_points(input))
print (implement_strategy_guide(input))
