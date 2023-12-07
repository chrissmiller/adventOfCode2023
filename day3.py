from collections import defaultdict
from helpers import get_lines

class PartNumber:
    def __init__(self, row: int, start: int, end: int, value: int):
        self.row = row
        self.start = start
        self.end = end
        self.value = value

    def __str__(self):
        return f"Row {self.row}, {self.start}:{self.end}"

def get_part_numbers_from_line(line: str, lineIndex: int) -> list[PartNumber]:
    '''
    Gets all part numbers in the current line
    :param line: The content of the line
    :param lineIndex: The index of the line
    :return: The list of partnumber objects in the line
    '''
    partNumbers = []
    isInNumber = False
    start = -1
    for i in range(len(line)):
        # start of new number
        if line[i].isdigit() and not isInNumber:
            start = i
            isInNumber = True
        # end of current number
        elif isInNumber and not line[i].isdigit():
            end = i-1
            isInNumber = False
            partNumbers.append(PartNumber(lineIndex, start, end, int(line[start:end+1])))
    if isInNumber:
        partNumbers.append(PartNumber(lineIndex, start, len(line)-1, int(line[start:len(line)])))

    return partNumbers

def is_symbol(char: str) -> bool:
    return not char.isalnum() and char != '.' and char != '\n'

def is_part_number_adjacent_to_symbol(part_number: PartNumber, lines: list[str], asterix_map: dict[[tuple[int,int]], list[int]]) -> bool:
    startRow = max(part_number.row - 1, 0)
    endRow = min(part_number.row + 1, len(lines)-1)
    startCol = max(part_number.start - 1, 0)
    endCol = min(part_number.end + 1, len(lines[0])-1)

    found_symbol = False
    for row in range(startRow, endRow + 1):
        for col in range(startCol, endCol + 1):
            # skip the actual number
            if row == part_number.row and part_number.start <= col <= part_number.end:
                continue

            if is_symbol(lines[row][col]):
                found_symbol = True
                update_asterix_map(row, col, part_number, lines, asterix_map)

    return found_symbol

def update_asterix_map(row: int, col: int, part_number: PartNumber, lines: list[str], asterix_map: dict[[tuple[int,int]], list[int]]):
    if lines[row][col] != '*':
        return
    if not (row,col) in asterix_map.keys():
        asterix_map[(row,col)] = [part_number.value]

    elif part_number.value not in asterix_map[(row,col)]:
        asterix_map[(row,col)] += [part_number.value]


def print_adjacency(startRow, endRow, startCol, endCol, lines):
    for row in range(startRow, endRow + 1):
        print(lines[row][startCol:endCol + 1])

def get_answer_part_one():
    lines = get_lines("data/day3.txt")
    answer = 0
    part_numbers = []
    for i in range(len(lines)):
        line_part_numbers = get_part_numbers_from_line(lines[i], i)
        part_numbers += line_part_numbers

    for part_number in part_numbers:
        if is_part_number_adjacent_to_symbol(part_number, lines, {}):
            answer += part_number.value

    return answer

def get_answer_part_two():
    lines = get_lines("data/day3.txt")
    answer = 0
    part_numbers = []
    for i in range(len(lines)):
        line_part_numbers = get_part_numbers_from_line(lines[i], i)
        part_numbers += line_part_numbers

    asterix_map = {}
    for part_number in part_numbers:
        is_part_number_adjacent_to_symbol(part_number, lines, asterix_map)

    # Filter to those mapped to exactly 2 parts
    sum_ratios = 0
    for key in asterix_map.keys():
        val = asterix_map[key]
        if len(val) == 2:
            sum_ratios += val[0] * val[1]

    return sum_ratios