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

def get_matches_for_card(card: Card) -> int:
    matches = 0
    for num in card.numbers:
        if num in card.winners:
            matches += 1

    return matches

def get_answer_part_one():
    lines = get_lines("data/day4_mini.txt")
    answer = 0
    for i in range(len(lines)):
        card = get_card_from_line(lines[i])
        points = get_points_for_card(card)
        answer += points

    return answer

def get_answer_part_two():
    lines = get_lines("data/day4.txt")
    answer = 0
    cards = [get_card_from_line(line) for line in lines]
    card_matches_map = {card.id:get_matches_for_card(card) for card in cards}

    # Maps from card ID to E2E value (number of generated cards, including self)
    max_id = cards[-1].id
    card_value_map = {max_id:1}

    # go back to front
    cards.reverse()
    for card in cards:
        if card.id in card_value_map.keys():
            print(f"For card {card.id}, using cached value ({card_value_map[card.id]}).")
            answer += card_value_map[card.id]
            continue
        card_value = 1
        points = card_matches_map[card.id]
        print(f"For card {card.id}, found {points} points. Running from {card.id+1} to {min(card.id+points, max_id)+1}.")
        for i in range(card.id+1, min(card.id+points, max_id)+1):
            print(f"For card {card.id}, adding E2E value of card {i} ({card_value_map[i]}).")
            card_value += card_value_map[i]

        card_value_map[card.id] = card_value
        answer += card_value
    return answer
