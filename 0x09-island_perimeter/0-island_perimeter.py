#!/usr/bin/python3
""" Module that calculates the perimeter of a grid """


def island_perimeter(grid):
    """ Returns the perimeter of an island """
    if not grid:
        return 0

    perimeteR = 0
    roWs, coLs = len(grid), len(grid[0])

    for i in range(roWs):
        for j in range(coLs):
            if grid[i][j] == 1:
                perimeteR += 4

                if i > 0 and grid[i - 1][j] == 1:
                    perimeteR -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeteR -= 2

    return perimeteR
