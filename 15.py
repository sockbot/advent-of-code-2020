lines = """1,2,16,19,18,0"""
# lines = """0,3,6"""
# lines = """1,3,2"""
# lines = """2,1,3"""
# lines = """1,2,3"""
# lines = """2,3,1"""
# lines = """3,2,1"""
# lines = """3,1,2"""
lines = lines.strip()
lines = [int(line) for line in lines.split(",")]

from helpers import timer
import copy


def diff(log, answer):
    lastTwo = [i for i, x in enumerate(log) if x == answer][-2:]
    return lastTwo[1] - lastTwo[0]


def getDiff(index, answer, diffLog):
    if answer not in diffLog:
        diffLog[answer] = [index]
        return 0

    if len(diffLog[answer]) == 1:
        diff = 0
    else:
        diff = diffLog[answer][1] - diffLog[answer][0]

    if diff not in diffLog:
        diffLog[diff] = [index]
    else:
        diffLog[diff] = [diffLog[diff][-1], index]

    return diff


def helper(lines, target):
    diffLog = {n: [i] for i, n in enumerate(lines)}
    log = copy.copy(lines)
    answer = log[-1]
    i = len(log)
    while i < target:
        answer = getDiff(i, answer, diffLog)
        i += 1
        if i % 1e6 == 0:
            print(i, answer)
    return answer


# @timer
def part1(lines):
    return helper(lines, 2020)


# @timer
def part2(lines):
    return helper(lines, 30e6)


print(f"Answer 1: {part1(lines)}")
print(f"Answer 2: {part2(lines)}")
