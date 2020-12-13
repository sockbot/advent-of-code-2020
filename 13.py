lines = """1001938
41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,431,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,17,x,19,x,x,x,x,x,x,x,x,x,x,x,863,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29
"""
# lines = """939
# 7,13,x,x,59,x,31,19"""
lines = lines.strip()
lines = [line for line in lines.split("\n")]
timestamp = int(lines[0])
routes = [route for route in lines[1].split(",")]


import copy
from helpers import timer

import math


def argMin(nextBusses):
    index = 0
    for j in range(len(nextBusses)):
        if nextBusses[j] == "x":
            continue
        if nextBusses[j] < nextBusses[index]:
            index = j
    return index


# @timer
def part1():
    nextBusses = []
    for route in routes:
        if route == "x":
            nextBusses.append(route)
            continue
        i = 0
        while i * int(route) < timestamp:
            i += 1
        nextBusses.append(i * int(route))
    print(routes)
    print(nextBusses)
    index = argMin(nextBusses)
    return (nextBusses[index] - timestamp) * int(routes[index])


# @timer
def part2():
    return


print(f"Answer 1: {part1()}")
print(f"Answer 2: {part2()}")
