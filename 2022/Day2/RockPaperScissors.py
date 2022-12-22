with open("input.txt","r",encoding="UTF-8") as input_file:
    lines = input_file.readlines()

choice_values = {
    "X":1,
    "Y":2,
    "Z":3
}

def check_win_draw_lose(opponent, my_choice):
    # A / X = rock, B / Y = paper, C / Z = scissors
    match(opponent):
        
        case "A":
            if my_choice == "X":
                return 3
            elif my_choice == "Y":
                return 6
            elif my_choice == "Z":
                return 0
        case "B":
            if my_choice == "X":
                return 0
            elif my_choice == "Y":
                return 3
            elif my_choice == "Z":
                return 6
        case "C":
            if my_choice == "X":
                return 6
            elif my_choice == "Y":
                return 0
            elif my_choice == "Z":
                return 3
    
def main():
    total = 0
    for line in lines:
        choices = line.strip().split(" ")
        my_choice_value = choice_values[choices[1]] 
        total += check_win_draw_lose(choices[0],choices[1]) + my_choice_value

    print(total)

if __name__ == "__main__()":
    main()