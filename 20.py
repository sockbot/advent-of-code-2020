from helpers import timer
import copy
import functools as ft

lines = """Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###..."""
lines = lines.strip()
tiles = [line.split("\n") for line in lines.split("\n\n")]


def isCornerTile(tile, tiles):
    matchCount = 0
    for edge in tile["edges"]:
        for targetTile in tiles:
            for targetEdge in targetTile["edges"]:
                if edge == targetEdge or edge == targetEdge[::-1]:
                    matchCount += 1
    return matchCount <= 3


def getCornerIds(tiles):
    cornerIds = []
    for tile in tiles:
        if isCornerTile(tile, tiles):
            cornerIds.append(int(tile["tileId"]))
    return cornerIds


# @timer
def part1(tiles):
    data = []
    for tile in tiles:
        tileId = tile[0][5:9]
        left = "".join(["".join(line[0]) for line in tile[1:]])
        right = "".join(["".join(line[9]) for line in tile[1:]])
        bottom = tile[len(tile) - 1]
        top = tile[1]
        data.append({"tileId": tileId, "edges": [top, bottom, left, right]})

    cornerIds = getCornerIds(data)
    return ft.reduce(lambda x, y: x * y, cornerIds, 0)


# @timer
def part2(tiles):
    return


print(f"Answer 1: {part1(tiles)}")
print(f"Answer 2: {part2(tiles)}")
