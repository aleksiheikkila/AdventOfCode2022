# Day 1: Calorie Counting
# https://adventofcode.com/2022/day/1

import heapq

TEST_INPUT = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""


# PART 1:
# how many Calories are being carried by the Elf carrying the most Calories?
def most_calories(inventory_file):
    max_calories = 0
    curr_calories = 0
    
    with open(inventory_file) as f:
        for line in f:
            if line.strip() == "":
                max_calories = max(max_calories, curr_calories)
                curr_calories = 0
            else:
                curr_calories += int(line.strip())

    return int(max(max_calories, curr_calories))


assert most_calories(r"./test_input.txt") == 24000

print(most_calories(r"./input.txt"))


## Part 2: Total calories for the top 3
# Lets generalize. Get top-N

class TopNLargest:
    """Keep top N largest values. Min heap"""
    def __init__(self, n: int):
        self.data = []
        self.n = n

    def add(self, val) -> None:
        #self.data.append(val)
        if len(self.data) >= self.n:
            #heapq.heapify(self.data)
            heapq.heappushpop(self.data, val)
        else:
            heapq.heappush(self.data, val)

    def get_top(self):
        return sorted(self.data, reverse=True)


def top_n_calories(inventory_file, n: int):
    top_values = TopNLargest(n=n)
    
    curr_calories = 0
    with open(inventory_file) as f:
        for line in f:
            if line.strip() == "":
                top_values.add(curr_calories)
                curr_calories = 0
            else:
                curr_calories += int(line.strip())  
    
    top_values.add(curr_calories)
    return top_values.get_top()


assert sum(top_n_calories("./test_input.txt", n=3)) == 45000

print(sum(top_n_calories("./input.txt", n=3)))



#### Part 2


