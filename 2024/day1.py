from collections import Counter

FILENAME = "input/day1.txt"


def read_file() -> (list[int], list[int]):
    A1, A2 = [], []
    with open(FILENAME, 'r') as file:
        for line in file:
            a, b = line.split()
            A1.append(int(a))
            A2.append(int(b))
    return A1, A2


def part1(A1: list[int], A2: list[int]) -> int:
    A1.sort()
    A2.sort()
    res = 0
    for a, b in zip(A1, A2):
        res += abs(a - b)
    return


def part2(A1: list[int], A2: list[int]) -> int:
    count = Counter(A2)
    res = 0

    for a in A1:
        res += a * count[a]
    return res
  

if __name__ == "__main__":
    A1, A2 = read_file()
    res = 0
    #res = part1(A1, A2)
    res = part2(A1, A2)

    print(res)