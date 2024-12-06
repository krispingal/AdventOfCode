FILENAME = "/Users/krishnababuji/src/misc/AdventOfCode/2024/input/day6.txt"


def read_file() -> (list[list[str]], tuple[int, int]):
    grid = []
    pos = (-1, -1)
    with open(FILENAME, 'r') as file:
        x = 0
        for line in file:
            row = list(line.strip())
            try:
                y = row.index('^')
                pos = (x, y)
            except ValueError:  # Intentionally ignoring this exception, no action required
                # flake8: noqa: E701
                pass
            grid.append(row)
            x += 1
    return grid, pos


def part1(grid: list[list[str]], pos) -> int:
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    cur_dir = 0
    r, c = pos
    m, n = len(grid), len(grid[0])
    res = 0
    while True:
        if grid[r][c] == '.':
            res += 1
            grid[r][c] = 'X'
        dr, dc = dirs[cur_dir]
        nr, nc = r + dr, c + dc
        if 0 > nr or nr >= m or 0 > nc or nc >= n: 
            break
        if grid[nr][nc] == '#':
            cur_dir = (cur_dir + 1) % 4
            continue
        r, c = nr, nc
    return res + 1


def part2(grid: list[list[str]], pos) -> int:
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    cur_dir = 0
    r, c = pos
    m, n = len(grid), len(grid[0])
    visited = set()
    # Mark all the cells the security might walk through
    while True:
        visited.add((r, c))
        dr, dc = dirs[cur_dir]
        nr, nc = r + dr, c + dc
        if 0 > nr or nr >= m or 0 > nc or nc >= n: 
            break
        if grid[nr][nc] == '#':
            cur_dir = (cur_dir + 1) % 4
            continue
        r, c = nr, nc
    res = 0
    r, c = pos
    # cannot place obstacle at starting point
    visited.remove((r, c))
    for tr, tc in visited:
        # Add an obstacle at one of the visited cells
        grid[tr][tc] = '#'
        r, c = pos
        cur_dir = 0
        # To check whether the path might cause a loop, have a set
        # which captures (x, y, cur_dir) if this combination exists
        # security entered a loop.
        t_visited = set()
        while True:
            if (r, c, cur_dir) in t_visited:
                res += 1
                break
            t_visited.add((r, c, cur_dir))
            dr, dc = dirs[cur_dir]
            nr, nc = r + dr, c + dc
            if 0 > nr or nr >= m or 0 > nc or nc >= n: 
                break
            if grid[nr][nc] == '#':
                cur_dir = (cur_dir + 1) % 4
                continue
            r, c = nr, nc
        # reset the grid, by removing the obstacle
        grid[tr][tc] = '.'
    return res


if __name__ == "__main__":
    grid, pos = read_file()
    #res1 = part1(grid, pos)
    res2 = part2(grid, pos)

    print(res2)
