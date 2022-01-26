#!/usr/bin/env python3
"""Bitburner - Spiralized Matrix solver

To run regression tests:

python3 -m doctest bb_sms.py

To run linting tests:

python3 -m pylint bb_sms.py"""

def entry_point(matrix: list) -> int:
    """Walk through the matrix, and append the current number to the result.

    >>> entry_point(
    ... [[1, 2, 3],
    ... [4, 5, 6],
    ... [7, 8, 9]])
    [1, 2, 3, 6, 9, 8, 7, 4, 5]

    >>> entry_point(
    ... [[14,38,32,47,47],
    ... [47,28,41,34,45],
    ... [39,17, 9,17,36],
    ... [31, 6,41,18,12],
    ... [10,46,26, 9,39],
    ... [ 4,26, 3, 2,24],
    ... [48,46,32,29,41]])
    [14, 38, 32, 47, 47, 45, 36, 12, 39, 24, 41, 29, 32, 46, 48, 4, 10, 31, \
39, 47, 28, 41, 34, 17, 18, 9, 2, 3, 26, 46, 6, 17, 9, 41, 26]
    """
    direction = "right"
    max_rows = len(matrix)
    max_cols = len(matrix[0])
    total_cells = max_rows * max_cols
    row_coord, col_coord, min_row, min_col = 0, 0, 0, 0
    answer = []
    while len(answer) < (total_cells):
        answer.append(matrix[row_coord][col_coord])
        if direction == "right":
            if col_coord == max_cols - 1:
                row_coord += 1
                min_row += 1
                direction = "down"
            else:
                col_coord += 1
        elif direction == "down":
            if row_coord == max_rows - 1:
                col_coord -= 1
                max_cols -= 1
                direction = "left"
            else:
                row_coord += 1
        elif direction == "left":
            if col_coord == min_col:
                row_coord -= 1
                max_rows -= 1
                direction = "up"
            else:
                col_coord -= 1
        else:
            if row_coord == min_row:
                col_coord += 1
                min_col += 1
                direction = "right"
            else:
                row_coord -= 1
    return answer


def main():
    """Main entry point"""
    lines = []
    while True:
        line = input("Enter the array: ")
        if line != '':
            line = line.replace('[', '').replace(']', '').replace(',', ' ')
            lines.append([int(_) for _ in line.split()])
        else:
            break
    print(f"Solution: {entry_point(lines)}")


if __name__ == "__main__":
    main()
