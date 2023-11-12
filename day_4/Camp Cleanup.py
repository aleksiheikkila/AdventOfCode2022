"""
Day 4: Camp Cleanup
https://adventofcode.com/2022/day/4
"""

# Part A: In how many assignment pairs does one range fully contain the other?


def count_fully_overlapping_pairs(input_file):
    rst = 0
    with open(input_file) as f:

        for line in f:
            rng1, rng2 = string_range_pair_to_tuple(line)

            if is_fully_overlapped_pair(rng1, rng2):
                rst += 1

    return rst


def string_range_pair_to_tuple(range_str: str) -> tuple:
    parts = range_str.strip().split(",")
    assert len(parts) == 2

    rng1 = string_range_to_tuple(parts[0])
    rng2 = string_range_to_tuple(parts[1])

    return (rng1, rng2)


def string_range_to_tuple(range_str: str) -> tuple:
    rng = range_str.strip().split("-")
    assert len(rng) == 2

    return (int(rng[0]), int(rng[1]))


def is_fully_overlapped_pair(range1: tuple, range2: tuple) -> bool:
    lo1, hi1 = range1
    lo2, hi2 = range2

    assert lo1 <= hi1
    assert lo2 <= hi2

    # range2 is covered:
    if lo1 <= lo2 and hi2 <= hi1:
        return True
    # range1 is covered:
    if lo2 <= lo1 and hi1 <= hi2:
        return True
    
    return False


assert count_fully_overlapping_pairs("test_input.txt") == 2


print("Part 1:", count_fully_overlapping_pairs("input.txt"))

##################
# Part 2:
# the Elves would like to know the number of pairs that overlap at all


def count_overlapping_pairs(input_file):
    rst = 0
    with open(input_file) as f:
        for line in f:
            rng1, rng2 = string_range_pair_to_tuple(line)

            if is_overlapping_pair(rng1, rng2):
                rst += 1

    return rst


def is_overlapping_pair(range1: tuple, range2: tuple) -> bool:
    lo1, hi1 = range1
    lo2, hi2 = range2

    assert lo1 <= hi1
    assert lo2 <= hi2

    # range1 below range2 or above range
    if hi1 < lo2 or hi2 < lo1:
        return False
    return True


assert count_overlapping_pairs("test_input.txt") == 4

print("Part 2:", count_overlapping_pairs("input.txt"))
