FILENAME = "input/day2.txt"


def read_file() -> list[int]:
    A = []
    with open(FILENAME, 'r') as file:
        for line in file:
            A.append([int(x) for x in line.split(" ")])
    return A


def part1(A: list[int]) -> int:
    res = 0
    for arr in A:
        res += is_safe(arr)
    return res


def is_safe(arr: list[int]) -> bool:
    if len(arr) <= 1:
        return True
    vals = set([a - b for a, b in zip(arr, arr[1:])])
    return vals <= {1,2,3} or vals <= {-1,-2,-3}


def part2(A: list[list[int]]) -> int:
    res = 0
    for arr in A:
        res += any(is_safe(arr[:i] + arr[i+1:]) for i in range(len(arr)))
    return res


if __name__ == "__main__":
    A = read_file()
    res = 0
    # res = part1(A)
    res = part2(A)

    print(res)