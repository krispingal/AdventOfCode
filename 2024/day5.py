from collections import defaultdict
FILENAME = "/Users/krishnababuji/src/misc/AdventOfCode/2024/input/day5.txt"


def read_file() -> (list[list[str]], list[list[str]]):
    edge_list, tests = [], []
    is_edge = True
    with open(FILENAME, 'r') as file:
        for line in file:
            if is_edge:
                if line == "\n":
                    is_edge = False
                else:
                    edge_list.append(line.strip().split('|'))
            else:
                tests.append(line.strip().split(','))
    return edge_list, tests


def part1(edge_list: list[list[str]], tests: list[list[str]]) -> int:
    graph = defaultdict(set)
    for u, v in edge_list:
        graph[u].add(v)

    res = 0
    for test in tests:
        test_set = set(test)
        local_rules = [(u, v) for u, v in edge_list if u in test_set and v in test_set]

        node_idx = {node: i for i, node in enumerate(test)}
        for u, v in local_rules:
            if node_idx[u] > node_idx[v]:
                break
        else:
            res += int(test[len(test)//2])

    return res


def topo_sort(test, local_rules):
    dag, indeg = defaultdict(list), defaultdict(int)
    for u, v in local_rules:
        dag[u].append(v)
        indeg[v] += 1
        indeg[u] = max(indeg[u], 0)

    q = [node for node in indeg if indeg[node] == 0]
    topo_order = []
    for node in q:
        topo_order.append(node)
        for nei in dag[node]:
            indeg[nei] -= 1
            if indeg[nei] == 0:
                q.append(nei)
    return topo_order


def part2(edge_list: list[list[str]], tests: list[list[str]]) -> int:
    graph = defaultdict(set)
    for u, v in edge_list:
        graph[u].add(v)

    res = 0
    for test in tests:
        test_set = set(test)
        local_rules = [(u, v) for u, v in edge_list if u in test_set and v in test_set]

        node_idx = {node: i for i, node in enumerate(test)}
        for u, v in local_rules:
            if node_idx[u] > node_idx[v]:
                corrected_order = topo_sort(test, local_rules)
                res += int(corrected_order[len(test)//2])
                break

    return res


if __name__ == "__main__":
    edge_list, tests = read_file()
    # res1 = part1(edge_list, tests)
    res2 = part2(edge_list, tests)

    print(res2)
