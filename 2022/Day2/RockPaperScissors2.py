import RockPaperScissors

def get_losing_move(opponent_move):
    # A / X = rock, B / Y = paper, C / Z = scissors
    if opponent_move == "A":
        return "Z"
    elif opponent_move == "B":
        return "X"
    else:
        return "Y"
    
def get_tie_move(opponent_move):
    # A / X = rock, B / Y = paper, C / Z = scissors
    if opponent_move == "A":
        return "X"
    elif opponent_move == "B":
        return "Y"
    else:
        return "Z"
    
def get_winning_move(opponent_move):
    # A / X = rock, B / Y = paper, C / Z = scissors
    if opponent_move == "A":
        return "Y"
    elif opponent_move == "B":
        return "Z"
    else:
        return "X"
    
def get_my_choice_from_strategy(opponent_move, strategy_input):
    # A / X = rock, B / Y = paper, C / Z = scissors
    match(strategy_input):
        case "X":
            return get_losing_move(opponent_move)
        case "Y":
            return get_tie_move(opponent_move)
        case "Z":
            return get_winning_move(opponent_move)

def get_my_choice_value(my_choice):
    return RockPaperScissors.choice_values[my_choice]

lines = RockPaperScissors.lines  
choice_values = RockPaperScissors.choice_values
check_win_draw_lose = RockPaperScissors.check_win_draw_lose

def main():
    total = 0
    for line in lines:
        choices = line.strip().split(" ")
        # Choices index 0 is opponents move, choices index 1 is strategy input
        my_choice = get_my_choice_from_strategy(choices[0], choices[1])
        total += check_win_draw_lose(choices[0],my_choice) + get_my_choice_value(my_choice)
        
    print (total)

if __name__ == "__main__":
    main()