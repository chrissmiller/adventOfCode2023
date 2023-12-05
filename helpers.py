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
        lines = f.readlines()
    finally:
        if f is not None:
            f.close()

    for i in range(len(lines)):
        lines[i] = lines[i].strip()

    return lines