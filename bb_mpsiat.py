#!/usr/bin/env python3
"""Bitburner - Minimum Path Sum in a Triangle

To run regression tests:

python3 -m doctest bb_mpsiat.py

To run linting tests:

python3 -m pylint bb_mpsiat.py"""


def entry_point(triangle: list) -> int:
    """Get the lowest path sum in the triangle

    >>> entry_point(
    ... [[9],
    ... [3,9],
    ... [6,4,4],
    ... [4,3,8,5],
    ... [5,8,1,8,2]])
    20

    >>> entry_point(
    ... [[2],
    ... [3,4],
    ... [6,5,7],
    ... [4,1,8,3]])
    11
    """
    previous_array = triangle[0]

    for row_counter in range(1, len(triangle)):
        next_array = []
        for column_counter in range(len(triangle[row_counter])):
            if column_counter == 0:
                next_array.append(previous_array[column_counter] + \
                                  triangle[row_counter][column_counter])
            elif column_counter == len(triangle[row_counter]) - 1:
                next_array.append(previous_array[column_counter - 1] + \
                                  triangle[row_counter][column_counter])
            else:
                next_array.append(min(previous_array[column_counter],
                                      previous_array[column_counter - 1]) + \
                                      triangle[row_counter][column_counter])
        previous_array = next_array
    return min(next_array)


def main():
    """Main entry point"""
    lines = []
    while True:
        line = input("Enter the triangle: ")
        if line != '':
            line = line.replace('[', '').replace(']', '').replace(',', ' ')
            lines.append([int(_) for _ in line.split()])
        else:
            break
    print(f"Solution: {entry_point(lines)}")


if __name__ == "__main__":
    main()
