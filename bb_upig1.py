#!/usr/bin/env python3
"""Bitburner contract solver - Unique Paths in Grid I.

To run regression tests:

python3 -m doctest bb-upig1.py

To run linting tests:

python3 -m pylint bb_upig1.py"""

def unique_paths(rows: int, columns: int) -> int:
    """Recursive function that returns the number of unique paths in a
    non-blocking grid.

    >>> unique_paths(9, 4)
    165

    >>> unique_paths(2, 3)
    3

    >>> unique_paths(9, 6)
    1287
    """
    if (rows == 1 or columns == 1):
        return 1
    return unique_paths(int(rows) - 1,
                        int(columns)) + unique_paths(int(rows), int(columns) - 1)


def main():
    """Main entry point"""
    rows = input("Rows: ")
    columns = input("Columns: ")
    print(f"Solution: {unique_paths(rows, columns)}")


if __name__ == "__main__":
    main()
