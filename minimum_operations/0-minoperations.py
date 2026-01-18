#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    Calculates the minimum number of Copy/Paste operations
    needed t reach exactly n H characters.

    Args:
        n (int): target number of characters

    Returns:
        int: minimum number of operations, or 0
    """
    if n < 2:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
