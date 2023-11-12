"""
Day 3: Rucksack Reorganization
https://adventofcode.com/2022/day/3
"""

from string import ascii_letters

LETTER_TO_PRIO = {letter: prio for prio, letter in enumerate(ascii_letters, start=1)}


##################################
# PART 1:

def find_common_element(rucksack: str) -> str:
    n = len(rucksack)
    assert n % 2 == 0
    
    comp_1, comp_2 = rucksack[:(n//2)], rucksack[(n//2):]

    # print(comp_1)
    # print(comp_2)

    elems_1_set = set(comp_1)
    elems_2_set = set(comp_2)

    # intersection
    common_elems = elems_1_set & elems_2_set

    # print(common_elems)
    if len(common_elems) != 1:
        raise ValueError
    
    return list(common_elems)[0]


def get_total_prio(input_file: str) -> int:
    total_prio = 0
    with open(input_file) as f:
        for line in f:
            common_elem = find_common_element(line.strip())
            total_prio += LETTER_TO_PRIO[common_elem]
    return total_prio


get_total_prio("./test_input.txt") == 157

# Answer to part 1:
print(get_total_prio("./input.txt"))


##################################
# PART 2:


TEST_DATA = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

# # Create a list of sets, one set for each string
# sets = [set(string) for string in strings]

# # Find the common characters by taking the intersection of all sets
# common_characters = set.intersection(*sets)

# # If you want the result as a list, convert the set back to a list
# common_characters_list = list(common_characters)


def get_total_group_badges_prio(input_file: str) -> int:
    total_prio = 0
    with open(input_file) as f:
        group_lines = []
        for linenum, line in enumerate(f, start=1):
            if linenum % 3 == 0:
                group_lines.append(line)
                badge = find_group_badge(group_lines)
                total_prio += LETTER_TO_PRIO[badge]
                group_lines = []
            else:
                group_lines.append(line)

    assert len(group_lines) == 0

    return total_prio


def find_group_badge(lines: list[str]) -> str:
    assert len(lines) == 3

    for i, line in enumerate(lines):
        if i == 0:
            common_elements = set(line.strip())
        else:
            common_elements = common_elements.intersection(set(line.strip()))

    assert len(common_elements) == 1, common_elements
    return common_elements.pop()



assert get_total_group_badges_prio("./test_input.txt") == 70

print("Part B answer:", get_total_group_badges_prio("./input.txt"))