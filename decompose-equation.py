# decompose an equation like
# w + w^2 + w^3 + ... + w^16 = -1
# into
# A = w + w^2 + w^4 + w^8 + ...
# B = w^3 + w^5 + w^6 + w^7 + ...
# thus A + B = -1, A * B = 4 (w + w^2 + ... + w^16) = -4
# where we used w^17 = 1
#
# parameters:
# EXPO = list of exponent LHS of equation
#           e.g. [1, 2, ..., 16]
# MOD   = number of sides of polygon, the number we mod
#           e.g. 17

from typing import List
from collections import Counter

MOD = 17
# EXPO = [1, 2, 3, 4, 5, 6, 7, 8, -1, -2, -3, -4, -5, -6, -7, -8]
# EXPO = [1, 2, 4, 8, -1, -2, -4, -8]
EXPO = [3, 5, 6, 7, -3, -5, -6, -7]
# MOD = 5
# EXPO = [1, 2, -1, -2]


def partition_list(source_list: List[int]) -> List[List[int]]:
    num_element = len(source_list)
    num_combination = 2 ** (
        num_element - 1
    )  # fix the last element in partition B, avoid duplicates
    result = []
    for i_comb in range(num_combination):
        partition_a = []
        partition_b = []
        for i_elem in range(num_element):
            if (i_comb >> i_elem) & 1:
                partition_a.append(source_list[i_elem])
            else:
                partition_b.append(source_list[i_elem])
        if partition_a and partition_b:
            result.append([partition_a.copy(), partition_b.copy()])
    return result


for partition_a, partition_b in partition_list(EXPO):
    # print(partition_a, partition_b)
    expansion = []
    for a in partition_a:
        for b in partition_b:
            expansion.append(a + b)
    # print("\t", expansion)

    count = Counter()
    for e in expansion:
        count[e % MOD] += 1
    # print("\t", count)

    count_total = sum(count.values())
    TARGET = list(range(1, MOD))
    factor = count_total // len(TARGET)
    if count_total == factor * len(TARGET):
        valid = True
        for e in TARGET:
            if (e % MOD) not in count:
                valid = False
                break
            count[e % MOD] -= factor
        for e in count:
            if count[e] != 0:
                valid = False
        if valid:
            print(
                "valid:\tA:",
                partition_a,
                "\tB:",
                partition_b,
                "\tA + B = RHS",
                "\tAB =",
                -factor,
            )
