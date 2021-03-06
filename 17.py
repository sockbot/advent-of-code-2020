from helpers import timer
import copy

lines = """
.#.
..#
###"""
lines = """
...#.#.#
..#..#..
#.#.##.#
###.##..
#####.##
#.......
#..#..##
...##.##"""

lines = lines.strip()
lines = [list(line) for line in lines.split("\n")]
world = [
    [[".", ".", "."], [".", ".", "."], [".", ".", "."]],
    lines,
    [[".", ".", "."], [".", ".", "."], [".", ".", "."]],
]

world = [
    [
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
    ],
    lines,
    [
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
    ],
]


def getActiveNeighbourCount(world, cubeCoord):
    count = 0
    for z in (-1, 0, 1):
        for y in (-1, 0, 1):
            for x in (-1, 0, 1):
                if x == 0 and y == 0 and z == 0:
                    continue
                k, j, i = cubeCoord
                if len(world) <= k + x or k + x < 0:
                    continue
                if len(world[0]) <= j + y or j + y < 0:
                    continue
                if len(world[0][0]) <= i + z or i + z < 0:
                    continue
                # print([k + x, j + y, i + z])
                # if k + x == 13 and j + y == 19 and i + z == 19:
                #     print(world)
                if world[k + x][j + y][i + z] == "#":
                    count += 1
    return count


def getNewWorld(oldWorld):
    newWorld = copy.deepcopy(oldWorld)

    # pad innermost array
    for i in range(len(newWorld)):
        for j in range(len(newWorld[0])):
            newWorld[i][j].insert(0, ".")
            newWorld[i][j].append(".")

    newWorld.insert(
        0,
        [
            ["." for coord in range(len(newWorld[0][0]))]
            for coord in range(len(newWorld[0]))
        ],
    )
    newWorld.append(
        [
            ["." for coord in range(len(newWorld[0][0]))]
            for coord in range(len(newWorld[0]))
        ],
    )

    for line in newWorld:
        line.insert(0, ["." for coord in range(len(line[0]))])
        line.append(["." for coord in range(len(line[0]))])

    oldWorld = copy.deepcopy(newWorld)
    # activate/deactivate the cubes
    for i in range(len(oldWorld[0][0])):
        for j in range(len(oldWorld[0])):
            for k in range(len(oldWorld)):
                anc = getActiveNeighbourCount(oldWorld, [k, j, i])
                if oldWorld[k][j][i] == "#":
                    if anc == 2 or anc == 3:
                        newWorld[k][j][i] = "#"
                    else:
                        newWorld[k][j][i] = "."
                else:  # if inactive
                    if anc == 3:
                        newWorld[k][j][i] = "#"
                    else:
                        newWorld[k][j][i] = "."
    return newWorld


# @timer
def part1(world):
    for i in range(6):
        world = getNewWorld(world)

    count = 0
    for i in range(len(world[0][0])):
        for j in range(len(world[0])):
            for k in range(len(world)):
                if world[k][j][i] == "#":
                    count += 1
    return count


# @timer
def part2(lines):
    return


print(f"Answer 1: {part1(world)}")
print(f"Answer 2: {part2(lines)}")
