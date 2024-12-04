"""Fabric area"""

from util.utils import read_input
from collections import Counter

def decompose_claim(claim):
    claim_split = claim.split()
    claim_id = claim_split[0]
    claim_offset = tuple(map(int, claim_split[2][:-1].split(',')))
    claim_area = tuple(map(int, claim_split[3].split('x')))
    return claim_id, claim_offset, claim_area

def get_fabric_grid(claim):
    _, claim_offset, claim_area = decompose_claim(claim)
    grid_pts = [ (x, y)
                 for x in range(claim_offset[1], (claim_offset[1] + claim_area[1]))
                 for y in range(claim_offset[0], (claim_offset[0] + claim_area[0]))
                 ]
    return grid_pts

def get_fabric_claim_grid(filename):
    fabric_claims = read_input(filename)
    fabric_claim_grid = Counter()
    for claim in fabric_claims:
        claimed_region = get_fabric_grid(claim)
        fabric_claim_grid.update(claimed_region)
    return fabric_claim_grid

def part1(filename):
    fabric_claim_grid = get_fabric_claim_grid(filename)
    return sum([1 for x in fabric_claim_grid.values() if x > 1])

def part2(filename):
    fabric_claim_grid = get_fabric_claim_grid(filename)
    fabric_single_claim = set([k for k in fabric_claim_grid if fabric_claim_grid[k] == 1])
    fabric_claims = read_input(filename)
    for claim in fabric_claims:
        claim_grid = set(get_fabric_grid(claim))
        if claim_grid.issubset(fabric_single_claim):
            claim_id, _, _ = decompose_claim(claim)
            return claim_id

if __name__ == '__main__':
    filename = f'data/day3/input'
    print('AOC Day 3')
    while True:
        response =int(input('Which part should be run ? press 0 to exit : '))
        if response == 1:
            print(part1(filename))
        elif response == 0:
            break
        elif response == 2:
            print(part2(filename))
