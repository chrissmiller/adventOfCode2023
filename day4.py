from collections import defaultdict
from helpers import get_lines

class Card:
    def __init__(self, id: int, winners: set[int], numbers: list[int]):
        self.id = id
        self.winners = winners
        self.numbers = numbers

    def __str__(self):
        return f"Card {self.id}, {self.winners}:{self.numbers}"

def get_card_from_line(line: str) -> Card:
    '''
    Gets the card in the current line
    :param line: The content of the line
    :return: The card
    '''
    id_s, id_e = line.index(' '), line.index(':')
    id = int(line[id_s+1:id_e])

    winners, numbers = line[id_e+1:].strip().split(' | ')
    winner_set = {int(winner) for winner in winners.strip().split(' ') if winner != ''}
    num_list = [int(num_str) for num_str in numbers.strip().split(' ') if num_str != '']

    return Card(id, winner_set, num_list)

def get_points_for_card(card: Card) -> int:
    points = 0
    for num in card.numbers:
        if num in card.winners:
            points = 1 if points == 0 else points*2

    return points

def get_answer_part_one():
    lines = get_lines("data/day4_mini.txt")
    answer = 0
    for i in range(len(lines)):
        card = get_card_from_line(lines[i])
        points = get_points_for_card(card)
        answer += points

    return answer

def get_answer_part_two():
    lines = get_lines("data/day4_mini.txt")
    answer = 0
    return "I don't know."