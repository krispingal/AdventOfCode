"""Polymer suit reduction"""
#from collections import deque


def part1(poly_str: str):
    fin_str = [poly_str[0]]
    for unit in poly_str[1:]:
        if fin_str and fin_str[-1] == unit.swapcase():
            _x = fin_str.pop()
        else:
            fin_str.append(unit)
    return len(fin_str)


def part2(poly_str: str):
    distinct_units = set([x for x in poly_str if x.islower()])
    min_length = 10000000000
    for unit in distinct_units:
        unit_set = set([unit, unit.upper()])
        _str = [x for x in poly_str if x not in unit_set]
        new_len = part1(_str)
        if new_len < min_length:
            min_length = new_len
    return min_length


def read_polymer_str(filename):
    _str: str = None
    with open(filename) as f:
        _str = ''.join(f.read().split('\n'))
        return _str

if __name__ == '__main__':
    filename = 'data/day5/input'
    print('AOC Day 5')
    polymer_str = read_polymer_str(filename)
    #polymer_str = 'aabAAB' #'dabAcCaCBAcCcaDA'
    while True:
        response = int(input('Which part should be run ? press 0 to exit : '))
        if response == 1:
            print(part1(polymer_str))
        elif response == 0:
            break
        elif response == 2:
            print(part2(polymer_str))
