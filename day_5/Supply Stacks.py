"""
Day 5: Supply Stacks
https://adventofcode.com/2022/day/5
"""

from collections import deque, defaultdict
from typing import NamedTuple

import re


def extract_numbers_from_string(input_string) -> list[int]:
    pattern = r'\b\d+\b'
    numbers = re.findall(pattern, input_string)
    return [int(num) for num in numbers]


class Move(NamedTuple):
    start: int
    end: int
    amount: int


def find_starting_state_lines(input_file) -> list[str]:
    state_lines = []

    with open(input_file) as f:
        for line in f:
            if "[" not in line:
                break
            state_lines.append(line.rstrip())
    
    return state_lines


def parse_starting_state(state_lines: list[str]) -> dict[deque]:
    state = defaultdict(deque)  # left is the top, right is the bottom

    for line in state_lines:
        line = line.rstrip()

        colnum = 1
        for i in range(0, len(line), 4):
            block = line[i:i+4].strip()
            if block != "":
                item = block.lstrip("[").rstrip("]")
                state[colnum].append(item)
            colnum += 1

    # sort
    state = dict(sorted(state.items()))

    return state


def parse_moves(input_file):
    moves = []
    in_moves_part = False  # have we yet passed the initial state part of the files?
    with open(input_file) as f:
        # get rid of the first rows
        for line in f:
            if in_moves_part:
                nums = extract_numbers_from_string(line.strip())
                moves.append(Move(start=nums[1], end=nums[2], amount=nums[0]))
            elif line.strip() == "":
                in_moves_part = True

    return moves


def process_stacked_move(move, state: defaultdict[deque]) -> defaultdict[deque]:
    """If needed, pick up a stack of items and move them in one go. Items retain their order"""
    crane_load = []
    # pick up
    for _ in range(move.amount):
        assert len(state[move.start]) > 0
        crane_load.append(state[move.start].popleft())

    # unload
    for item in reversed(crane_load):
        state[move.end].appendleft(item)

    return state


def process_move(move, state: defaultdict[deque]) -> defaultdict[deque]:
    """move on by one, i.e. pick one, deliver it, pick up next, ..."""
    for _ in range(move.amount):
        assert len(state[move.start]) > 0

        state[move.end].appendleft(state[move.start].popleft())

    return state


def get_topmost_items(state) -> str:
    topmost_items = []

    min_col = min(int(colnum) for colnum in state.keys())
    max_col = max(int(colnum) for colnum in state.keys())

    for colnum in range(min_col, max_col + 1):
        if len(state[colnum]) == 0:
            topmost_items.append("")
        else:
            topmost_items.append(state[colnum][0])
    return "".join(topmost_items)


def init(file):
    starting_state = find_starting_state_lines(file)
    state = parse_starting_state(starting_state)
    moves = parse_moves(file)
    return state, moves


#############################################
# Test cases
TEST_FILE = "test_input.txt"

# For part 1
state, moves = init(TEST_FILE)
for move in moves:
    state = process_move(move=move, state=state)
assert get_topmost_items(state) == "CMZ"

# For part 2
state, moves = init(TEST_FILE)
for move in moves:
    state = process_stacked_move(move=move, state=state)
assert get_topmost_items(state) == "MCD"


#############################################
INPUT_FILE = "input.txt"

# Part 1 solution
print("\nPART 1:")
state, moves = init(INPUT_FILE)
for move in moves:
    state = process_move(move=move, state=state)

topmost_items = get_topmost_items(state)
print(topmost_items)


# Part 2
print("\nPART 2:")
state, moves = init(INPUT_FILE)
for move in moves:
    state = process_stacked_move(move=move, state=state)

topmost_items = get_topmost_items(state)
print(topmost_items)
