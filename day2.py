"""Validate Checksum"""
from util.utils import read_input
from collections import Counter

def part1(filename):
    ids = read_input(filename)
    num_twice, num_thrice = 0, 0
    for id in ids:
        cntr = Counter(id)
        if 2 in cntr.values():
            num_twice += 1
        if 3 in cntr.values():
            num_thrice += 1
    return num_twice * num_thrice

def part2(filename):
    ids = read_input(filename)
    first_id = next(ids)
    id_len = len(first_id)
    id_collection = set()
    id1, id2 = None, None
    for id in ids:
        for prior_id in id_collection:
            mismatch = 0
            for idx in range(id_len):
                if id[idx] != prior_id[idx]:
                    mismatch += 1
                    if mismatch > 1:
                        continue
            if mismatch == 1:
                id1, id2 = id, prior_id
                break
        id_collection.add(id)
    return ''.join([x for x, y in zip(id1, id2) if x == y])

if __name__ == '__main__':
    filename = f'data/day2/input'
    print('AOC Day 2')
    while True:
        response =int(input('Which part should be run ? press 0 to exit : '))
        if response == 1:
            print(part1(filename))
        elif response == 0:
            break
        elif response == 2:
            print(part2(filename))
