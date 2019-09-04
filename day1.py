if __name__ == '__main__':
    filename = f'data/day1/input'
    with open(filename) as f:
        freq = 0
        for line in f:
            freq += int(line)
    print(freq)
