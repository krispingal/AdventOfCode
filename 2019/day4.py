"""Sneaking past sleeping guards"""
import re

from datetime import datetime
from util.utils import read_input
from collections import Counter, defaultdict

guard_pattern = re.compile('(?<=Guard #)\d+')
time_pattern = re.compile('\d{4}-\d{2}-\d{2} \d{2}:\d{2}')


class GuardDuty:

    def __init__(self):
        self.guard_on_duty = None
        self.guard_sleep_dict = defaultdict(int)
        self.minute_log = defaultdict(int)
        self.guard_asleep_since = None


    def process_log(self, log):
        time = self.get_log_minute(log)
        if 'begins shift' in log:
            guard = guard_pattern.search(log)
            new_guard = guard.group(0)
            self.guard_on_duty = new_guard
            self.guard_asleep_since = None
        elif 'wakes up' in log and self.guard_asleep_since is not None:
            for i in range(self.guard_asleep_since, time):
                self.guard_sleep_dict[self.guard_on_duty] += 1
                self.minute_log[(self.guard_on_duty, i)] += 1
            self.guard_asleep_since = None
        elif 'falls asleep' in log:
            self.guard_asleep_since = time

    def get_log_minute(self, log):
        m = time_pattern.search(log)
        minute = m.group(0).split(':')[-1]
        return int(minute)

def argmax(d):
    k = max(d, key=d.get)
    return k, d[k]

def get_guard_duty_log(filename):
    guard_duty = GuardDuty()
    guard_logs = read_input(filename)
    for log in guard_logs:
        guard_duty.process_log(log)
    return guard_duty


def part1(guard_log):
    max_sleep_guard, _count = argmax(guard_log.guard_sleep_dict)
    (_, most_slept_min), count = argmax({(x, y) : guard_log.minute_log[(x, y)] for (x, y) in guard_log.minute_log if x == max_sleep_guard})
    print(max_sleep_guard, most_slept_min)
    result = int(max_sleep_guard) * most_slept_min
    return result

def part2(guard_log):
    (max_sleep_guard, max_slept_min), count = argmax(guard_log.minute_log)
    return int(max_sleep_guard) * max_slept_min

def sort_file(filename):
    logs = []
    with open(filename, 'r') as f:
        for line in f:
            logs.append(line)
    sorted_logs = sorted(logs, key=lambda x: get_sort_key(x))
    file_loc = '/'.join(filename.split('/')[:-1])+'/'
    sorted_input_file = file_loc + 'sorted_input'
    print(sorted_input_file)
    with open(sorted_input_file, 'w') as out:
        for log in sorted_logs:
            out.write(log)
    return sorted_input_file


def get_sort_key(log):
    m = time_pattern.search(log)
    extracted_time = datetime.strptime(m.group(0), '%Y-%m-%d %M:%S')
    return extracted_time

if __name__ == '__main__':
    filename = 'data/day4/input'
    print('AOC Day 4')
    sorted_input = sort_file(filename)
    #sorted_input = 'data/day4/proto/sorted_input'
    print('Sort completed!')
    guard_log = get_guard_duty_log(sorted_input)
    while True:
        response = int(input('Which part should be run ? press 0 to exit : '))
        if response == 1:
            print(part1(guard_log))
        elif response == 0:
            break
        elif response == 2:
            print(part2(guard_log))
