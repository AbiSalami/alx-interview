#!/usr/bin/python3
"""N queens solution finder module.
"""
import sys


def get_input():
    """Retrieves and validates this program's argument.

    Returns:
        int: The size of the chessboard.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def is_attacking(pos0, pos1):
    """Checks if the positions of two queens are in an attacking mode.

    Args:
        pos0 (tuple): The first queen's position.
        pos1 (tuple): The second queen's position.

    Returns:
        bool: True if the queens are in an attacking position else False.
    """
    same_row = pos0[0] == pos1[0]
    same_col = pos0[1] == pos1[1]
    same_diag = abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1])
    return same_row or same_col or same_diag


def solution_exists(solutions, new_solution):
    """Checks if a solution already exists in the list of solutions.

    Args:
        solutions (list of lists): The list of existing solutions.
        new_solution (list of tuples): The new solution to check.

    Returns:
        bool: True if it exists, otherwise False.
    """
    return any(set(solution) == set(new_solution) for solution in solutions)


def build_solutions(n, row, current_solution, solutions, positions):
    """Builds solutions recursively for the N queens problem.

    Args:
        n (int): The size of the chessboard.
        row (int): The current row being filled with a queen.
        current_solution (list of tuples): The current positions of queens.
        solutions (list of lists): The list to store all valid solutions.
        positions (list of tuples): All possible positions on the chessboard.
    """
    if row == n:
        if not solution_exists(solutions, current_solution):
            solutions.append(current_solution.copy())
        return

    for col in range(n):
        new_position = (row, col)
        if not any(is_attacking(new_position, queen_pos) for queen_pos in current_solution):
            current_solution.append(new_position)
            build_solutions(n, row + 1, current_solution, solutions, positions)
            current_solution.pop()


def get_solutions(n):
    """Gets all solutions for the N queens problem.

    Args:
        n (int): The size of the chessboard.

    Returns:
        list of lists: A list containing all solutions.
    """
    solutions = []
    positions = [(i // n, i % n) for i in range(n ** 2)]
    build_solutions(n, 0, [], solutions, positions)
    return solutions


# Main execution
n = get_input()
solutions = get_solutions(n)
for solution in solutions:
    print(solution)

