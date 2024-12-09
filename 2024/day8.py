from math import gcd
from collections import defaultdict
FILENAME = "/Users/krishnababuji/src/misc/AdventOfCode/2024/input/day8.txt"


def read_file() -> list[list[str]]:
    grid = []
    with open(FILENAME, 'r') as file:
        for line in file:
            grid.append(list(line.strip()))
    return grid


def part1(grid: list[list[str]]) -> int:
    m, n = len(grid), len(grid[0])
    
    def inside_grid(p):
        return 1 if 0 <= p[0] < m and 0 <= p[1] < n else 0
    
    freq_map = defaultdict(list)
    for i in range(m):
        for j in range(n):
            if grid[i][j] != '.':
                freq_map[grid[i][j]].append((i, j))
    anti_nodes = set()
    for freq in freq_map:
        locs = freq_map[freq]
        for i in range(len(locs)):
            for j in range(i):
                x1, y1 = locs[i]
                x2, y2 = locs[j]
                a1 = 2 * x1 - x2, 2 * y1 - y2
                a2 = 2 * x2 - x1, 2 * y2 - y1
                if inside_grid(a1):
                    anti_nodes.add(a1)
                if inside_grid(a2):
                    anti_nodes.add(a2)
    return len(anti_nodes)


def part2(grid: list[list[str]]) -> int:
    m, n = len(grid), len(grid[0])
    
    def inside_grid(p):
        return 1 if 0 <= p[0] < m and 0 <= p[1] < n else 0
    
    freq_map = defaultdict(list)
    for i in range(m):
        for j in range(n):
            if grid[i][j] != '.':
                freq_map[grid[i][j]].append((i, j))
    anti_nodes = set()
    for freq in freq_map:
        locs = freq_map[freq]
        for i in range(len(locs)):
            for j in range(i):
                x1, y1 = locs[i]
                x2, y2 = locs[j]

                dx, dy = x2 - x1, y2 - y1
                gcd_val = gcd(dx, dy)
                step_x, step_y = dx // gcd_val, dy // gcd_val
                x, y = x1, y1
                while inside_grid(((x, y))):
                    anti_nodes.add((x, y))
                    x += step_x
                    y += step_y
                x, y = x2, y2
                while inside_grid(((x, y))):
                    anti_nodes.add((x, y))
                    x -= step_x
                    y -= step_y
        anti_nodes.update(locs)
    return len(anti_nodes)


if __name__ == "__main__":
    grid = read_file()
    # print(grid)
    # res1 = part1(grid)
    res2 = part2(grid)

    print(res2)