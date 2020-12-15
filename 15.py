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

# diffLog = {0: [0], 3: [1], 6: [2]}
diffLog = {1: [0], 2: [1], 16: [2], 19: [3], 18: [4], 0: [5]}


def diff(log, answer):
    lastTwo = [i for i, x in enumerate(log) if x == answer][-2:]
    return lastTwo[1] - lastTwo[0]


# @timer
def part1(lines):
    log = copy.copy(lines)
    answer = log[-1]
    i = len(log)
    while i < 2020:
        if log.count(answer) <= 1:
            answer = 0
        else:
            answer = diff(log, answer)
        log.append(answer)
        i += 1
    return answer


# def updateDiffLog(diff):


def getDiff(index, answer):
    if answer not in diffLog:
        diffLog[answer] = [index]
        return 0
    if len(diffLog[answer]) == 1:
        diff = 0
        if diff not in diffLog:
            diffLog[diff] = [index]
        elif len(diffLog[diff]) == 1:
            diffLog[diff].append(index)
        else:
            diffLog[diff] = [diffLog[diff][1], index]
        return diff
    if len(diffLog[answer]) == 2:
        diff = diffLog[answer][1] - diffLog[answer][0]
        if diff not in diffLog:
            diffLog[diff] = [index]
        elif len(diffLog[diff]) == 1:
            diffLog[diff].append(index)
        else:
            diffLog[diff] = [diffLog[diff][1], index]
        return diff

    diff = diffLog[answer][1] - diffLog[answer][0]
    if diff not in diffLog:
        diffLog[diff] = [index]
    elif len(diffLog[diff]) <= 1:
        diffLog[diff].append(index)
    else:
        diffLog[diff] = [diffLog[diff][1], index]
    return diff


# @timer
def part2(lines):
    log = copy.copy(lines)
    answer = log[-1]
    i = len(log)
    while i < 2020:
        answer = getDiff(i, answer)
        i += 1
        if i % 1000000 == 0:
            print(i, answer)
    return answer


print(f"Answer 1: {part1(lines)}")
print(f"Answer 2: {part2(lines)}")
