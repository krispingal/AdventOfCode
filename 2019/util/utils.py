def read_input(filename: str):
    """ Reads input filename and yields line by line"""
    with open(filename) as f:
        for line in f:
            yield line