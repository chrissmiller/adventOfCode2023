def get_calibration_value_for_line_part_one(line: str) -> int:
    '''
    Gets the calibration value for a single line
    :param line: The string line
    :return: The calibration value
    :raises: ValueError, if no digits
    '''
    val = 0
    for ch in line:
        if ch.isdigit():
            val = 10 * int(ch)
            break

    for ch in reversed(line):
        if ch.isdigit():
            val += int(ch)
            break
    if val == 0:
        raise ValueError("No digits in line.")
    return val

def get_lines(filepath: str) -> list[str]:
    '''
    Gets the lines in the provided filepath
    :param filepath: The path to the file
    :return: The list of lines in the file
    :raises: FileNotFoundError
    '''
    f = None
    try:
        f = open(filepath, "r")
        return f.readlines()
    finally:
        if f is not None:
            f.close()

def get_answer_part_one() -> int:
    lines = get_lines("data/day1.txt")
    answer = 0
    for line in lines:
        answer += get_calibration_value_for_line_part_one(line)

    return answer


def get_answer_part_one() -> int:
    lines = get_lines("data/day1.txt")
    answer = 0
    for line in lines:
        answer += get_calibration_value_for_line_part_one(line)

    return answer

def get_val_at_point(line: str, index: int, reverse: bool = False) -> int:
    digit_map = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
    if line[index].isdigit():
        return int(line[index])

    current_line_substring = line[index:] if reverse else line[:index+1]
    for digit_str in digit_map.keys():
        if digit_str in current_line_substring:
            return digit_map[digit_str]
    return None

def get_calibration_value_for_line_part_two(line: str) -> int:
    '''
    Gets the calibration value for a single line
    :param line: The string line
    :return: The calibration value
    :raises: ValueError, if no digits
    '''
    val = 0
    for i in range(len(line)):
        val = get_val_at_point(line, i, reverse=False)
        if val is not None:
            val = 10*val
            break

    for i in range(len(line) - 1, -1, -1):
        reverse_val = get_val_at_point(line, i, reverse=True)
        if reverse_val is not None:
            val += reverse_val
            break

    if val == 0:
        raise ValueError("No digits in line.")
    return val

def get_answer_part_two() -> int:
    lines = get_lines("data/day1.txt")
    answer = 0
    for line in lines:
        answer += get_calibration_value_for_line_part_two(line.lower())

    return answer
