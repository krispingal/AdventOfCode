""" Day1 of Advent of Code"""

from util.utils import read_input

def part1(filename):
    """Find the resulting freq"""
    freq = 0
    changing_freq = read_input(filename)
    for change in changing_freq:
        freq += int(change)
    return freq

def part2(filename):
    """Find the first repeating frequency"""
    #Use sets to be faster
    freq_list = set([0])
    freq = 0
    while True:
        changing_freq = read_input(filename)
        for change in changing_freq:
            freq += int(change)
            if freq not in freq_list:
                freq_list.add(freq)
            else:
                return freq

if __name__ == '__main__':
    filename = f'data/day1/input'
    print('AOC Day 1')
    while True:
        response =int(input('Which part should be run ? press 0 to exit : '))
        if response == 1:
            print(part1(filename))
        elif response == 0:
            break
        elif response == 2:
            print(part2(filename))

