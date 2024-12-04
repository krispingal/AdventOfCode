import re

FILENAME = "input/day3.txt"


def read_file() -> str:
    with open(FILENAME, 'r') as file:
        return file.read()


def part1(s: str) -> int:
    p = re.compile(r"mul\((?P<a>\d+),(?P<b>\d+)\)")
    res = 0
    matches = p.finditer(s)
    for m in matches:
        res += int(m.group('a')) * int(m.group('b'))
    return res


def part2(s: str) -> int:
    # Find all  muls between "don't()" and "do()". 
    # We can subtract them from total to get result of part2
    p2 = re.compile(r"don't\(\)(?P<trg>.*?)(?:do\(\)|$)", re.DOTALL)
    res = 0
    matches_trg = p2.finditer(s)
    for m_trg in matches_trg:
        res += part1(m_trg.group('trg'))
    return res


if __name__ == "__main__":
    s = read_file()
    res1 = part1(s)
    res2 = part2(s)

    print(res1 - res2)
