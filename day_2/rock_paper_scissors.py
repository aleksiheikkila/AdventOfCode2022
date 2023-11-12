"""
Day 2: Rock Paper Scissors
https://adventofcode.com/2022/day/2
"""

# Could use Enum

OPPONENT_ENUM_TO_MINE = {
    "A": "X",
    "B": "Y",
    "C": "Z",
}

# You: 
# X for Rock, Y for Paper, and Z for Scissors

# Opponent: 
# A for Rock, B for Paper, and C for Scissors


##################################
# PART 1:

def score_round(opp: str, you: str) -> int:
    if you == "X":  # Rock
        score = 1
    elif you == "Y":  # Paper
        score = 2
    elif you == "Z":  # Scissor
        score = 3
    else:
        raise ValueError
    
    # Draw
    if OPPONENT_ENUM_TO_MINE[opp] == you:
        return score + 3
    
    # Lose
    elif (opp == "A" and you == "Z") or (opp == "B" and you == "X") or (opp == "C" and you == "Y"):
        return score
    # Win
    else:
        return score + 6


def score_game(input_file: str) -> int:
    total_score = 0
    with open(input_file) as f:
        for line in f:
            opp, you = line.strip().split()
            # score = score_round(opp, you)
            # print(score)
            total_score += score_round(opp, you)

    return total_score


assert score_game("./test_input.txt") == 15

# Answer to part 1:
print(score_game("./input.txt"))


##################################
# PART 2:

# the second column says how the round needs to end: 
# X means you need to lose, 
# Y means you need to end the round in a draw, 
# and Z means you need to win.


# You: 
# X for Rock, Y for Paper, and Z for Scissors

# Opponent: 
# A for Rock, B for Paper, and C for Scissors


def get_gesture(opp: str, outcome: str) -> str:
    # DRAW:
    if outcome == "Y":
        return OPPONENT_ENUM_TO_MINE[opp]
    
    # Need to LOSE:
    if outcome == "X":
        if opp == "A":
            return "Z"
        if opp == "B":
            return "X"
        if opp == "C":
            return "Y"
        else:
            raise ValueError

    # Need to WIN:  
    else:
        if opp == "A":
            return "Y"
        if opp == "B":
            return "Z"
        if opp == "C":
            return "X"
        else:
            raise ValueError


def score_game2(input_file: str) -> int:
    total_score = 0
    with open(input_file) as f:
        for line in f:
            opp, outcome = line.strip().split()
            you = get_gesture(opp, outcome)
            # score = score_round(opp, you)
            # print(score)
            total_score += score_round(opp, you)

    return total_score


assert score_game2("./test_input.txt") == 12

# Answer to part 2:
print(score_game2("./input.txt"))
