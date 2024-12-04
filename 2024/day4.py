FILENAME = "/Users/krishnababuji/src/misc/AdventOfCode/2024/input/day4.txt"

dirs = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
STR = "XMAS"


def read_file() -> list[list[str]]:
    M = []
    with open(FILENAME, 'r') as file:
        for line in file:
            M.append(line.strip())
    return M


def part1(M: list[list[str]]) -> int:
    m, n = len(M), len(M[0])

    def dfs(r, c, cur, dir) -> bool:
        if 0 > r or r >= m or 0 > c or c >= n or M[r][c] != STR[cur]:
            return False
        if cur == 3:
            return M[r][c] == STR[cur]
        nr, nc = r + dirs[dir][0], c + dirs[dir][1]
        return dfs(nr, nc, cur+1, dir)

        return dfs
    ans = 0
    for i in range(m):
        for j in range(n):
            if M[i][j] == 'X':
                for x, dir in enumerate(dirs):
                    di, dj = dir
                    ni, nj = i + di, j + dj
                    temp = dfs(ni, nj, 1, x)
                    ans += temp
    return ans


def part2(s: str) -> int:
    m, n = len(M), len(M[0])
    ans = 0
    for i in range(1, m-1):
        for j in range(1, n-1):
            # capture all diagonal element values as a set
            values = {M[i-1][j-1], M[i+1][j+1], M[i+1][j-1], M[i-1][j+1]}
            # check whether diagonal endpoints have different values, and 
            # unique values are 'M' and 'S' - if value is 'A'
            if (M[i][j] == 'A' and M[i-1][j-1] != M[i+1][j+1] and
                    M[i+1][j-1] != M[i-1][j+1] and values == {'M', 'S'}):
                ans += 1
    return ans


if __name__ == "__main__":
    M = read_file()
    # res1 = part1(M)
    res2 = part2(M)

    print(res2)
