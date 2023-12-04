from helpers import get_lines

class Game:
    def __init__(self, id: int, rounds: list[dict[str, int]]):
        self.id = id
        self.rounds = rounds

    def __str__(self):
        return f"ID: {self.id}. Rounds: {self.rounds}."

def get_round_from_str(round_str: str) -> dict[str, int]:
    round = {}
    counts = round_str.split(',')
    for count in counts:
        split_values = count.strip().split(' ')
        if len(split_values) != 2:
            print(f"Unexpected values! {split_values}.")
            raise ValueError("Unexpected count of split round values")
        num, color = split_values
        round[color] = int(num)

    return round

def get_game_from_line(line: str) -> Game:
    '''
    Parses a game's information from the string representation
    :param line:
    :return:
    :raises: ValueError on unexpected format
    '''
    line_semicolon_index = line.index(':')
    id = int(line[5:line_semicolon_index])
    round_strs = line[line_semicolon_index+1:].split(';')
    rounds = []
    for round_str in round_strs:
        rounds.append(get_round_from_str(round_str))

    return Game(id, rounds)

def is_game_valid(limits: dict[str, int], game: Game) -> bool:
    for round in game.rounds:
        for limit in limits.keys():
            # Check if the round has a matching color and it exceeds the limit
            if limit in round.keys() and round[limit] > limits[limit]:
                return False
    return True

def get_answer_part_one():
    lines = get_lines("data/day2.txt")
    limits = {"red": 12, "blue": 14, "green": 13}
    answer = 0
    for line in lines:
        game = get_game_from_line(line)
        if is_game_valid(limits, game):
            answer += game.id
    return answer

def get_answer_part_two():
    lines = get_lines("data/day2_mini.txt")
    return "Not implemented!"