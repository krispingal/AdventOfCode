FILENAME = "/Users/krishnababuji/src/misc/AdventOfCode/2024/input/day7.txt"


def read_file() -> list[tuple[int, list[int]]]:
    equations = []
    with open(FILENAME, 'r') as file:
        for line in file:
            k, vals = line.strip().split(':')
            equations.append((int(k), [int(i) for i in vals.split()]))
    return equations


def part1(equations: list[tuple[int, list[int]]]) -> int:
    res = 0

    def is_possible(k, vals, cur) -> bool:
        n = len(vals)
        if cur > k: return False
        if not n:
            return k == cur
        return is_possible(k, vals[1:], cur * vals[0]) or is_possible(k, vals[1:], cur + vals[0])
        
    for eqn in equations:
        k, vals = eqn
        if is_possible(k, vals[1:], vals[0]):
            res += k
    return res


def part2(equations: list[tuple[int, list[int]]]) -> int:
    res = 0

    def is_possible(k, vals, cur) -> bool:
        n = len(vals)
        if cur > k: return False
        if not n:
            return k == cur
        v1 = cur * vals[0]
        v2 = cur + vals[0]
        v3 = int(str(cur) + str(vals[0]))
        return any([is_possible(k, vals[1:], v1), is_possible(k, vals[1:], v2), is_possible(k, vals[1:], v3)])
        
    for eqn in equations:
        k, vals = eqn
        if is_possible(k, vals[1:], vals[0]):
            res += k
    return res


if __name__ == "__main__":
    eqn = read_file()
    #res1 = part1(eqn)
    res2 = part2(eqn)

    print(res2)
