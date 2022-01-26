#!/usr/bin/env python3
"""Bitburner - Solve the Total Ways to Sum contract.

To run regression tests:

python3 -m doctest bb_twts.py"""


def entry_point(target: int) -> int:
    """Get number of possible combinations

    >>> entry_point(3)
    2

    >>> entry_point(4)
    4

    >>> entry_point(7)
    14

    >>> entry_point(61)
    1121504
    """
    ways = []
    ways.append(1)
    target += 1
    for current_number in range(1, target):
        ways.append(0)
    for current_number in range(1, target - 1):
        for next_number in range(current_number, target):
            ways[next_number] += ways[next_number - current_number]
    return ways[target - 1]


def main():
    """Main entry point"""
    target = int(input("Enter your target number: "))
    print(f"Solution: {entry_point(target)}")


if __name__ == "__main__":
    main()
