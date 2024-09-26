#!/usr/bin/python3
"""Island perimeter module.
This module contains the function `island_perimeter`
which computes the perimeter of an island represented by a grid.
"""


def island_perimeter(grid):
    """Computes the perimeter of an island with no lakes.
    
    Args:
        grid (list): A list of lists of integers representing the island.
                     0 represents water, and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    n = len(grid)
    
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 1:
                # Check each direction (up, right, down, left)
                if i == 0 or grid[i - 1][j] == 0:  # Up
                    perimeter += 1
                if j == len(row) - 1 or grid[i][j + 1] == 0:  # Right
                    perimeter += 1
                if i == len(grid) - 1 or grid[i + 1][j] == 0:  # Down
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:  # Left
                    perimeter += 1
                    
    return perimeter

