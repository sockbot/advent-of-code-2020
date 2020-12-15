lines = """1,2,16,19,18,0"""
# lines = """0,3,6"""
lines = """1,2,16,19,18,0"""
# lines = """0,3,6"""
# lines = """0,3,6"""
# lines = """0,3,6"""
# lines = """0,3,6"""
# lines = """0,3,6"""
lines = lines.strip()
lines = [int(line) for line in lines.split(",")]

from helpers import timer
import copy


def diff(log, answer):
    lastTwo = [i for i, x in enumerate(log) if x == answer][-2:]
    return lastTwo[1] - lastTwo[0]


# @timer
def part1(lines):
    # print(lines)
    answer = 6
    log = copy.copy(lines)
    i = len(log)
    while i < 30000000:
        if log.count(answer) <= 1:
            answer = 0
        else:
            answer = diff(log, answer)
        log.append(answer)
        i += 1
        # print(i, answer)
    return answer


# @timer
def part2(lines):
    return


print(f"Answer 1: {part1(lines)}")
print(f"Answer 2: {part2(lines)}")
