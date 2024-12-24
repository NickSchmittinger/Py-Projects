import random
from typing import List

default_min_range = 1
default_max_range = 100

def start_game_print():
    print("Your guess will evaluate higher or lower for each index of the number.")
    print("Score includes: total numbers completed, indexes completed, and guess count.")
    print("Type quit, no, or stop to end the game.")

def generate_num(min: int = default_min_range, max: int = default_max_range) -> int:
    num: int = random.randint(min, max)
    print("\nA new number has been generated!\nIt is between: " + str(min) + " and " + str(max) + "\n")
    return num

def num_to_list(num: int) -> List[int]:
    return [int(x) for x in str(num)]

def guess(player_guess: str) -> bool: 
    if player_guess.isnumeric():
        guess_num_as_list: List[int] = [int(x) for x in str(player_guess)]
        lists_compared_size: int = len(guess_num_as_list) - len(generated_num_as_list)
        if lists_compared_size > 0:
            print("Your guess was over the size of the number by " + str(abs(lists_compared_size)) + " digits.")
            return False
        elif lists_compared_size < 0:
            print("Your guess was under the size of the number by " + str(abs(lists_compared_size)) + " digits.")
            return False
        
        compared_list: List[bool] = []
        for i in range(len(guess_num_as_list)):
            compared_list.append(compare_nums(generated_num_as_list[i], guess_num_as_list[i], str(i)))
        #print(str(compared_list))
        if False in compared_list:
            current_num_list: List[str] = []
            for i in range(len(guess_num_as_list)):
                if compared_list[i] == False:
                    current_num_list.append("x")
                else:
                    current_num_list.append(str(guess_num_as_list[i]))
            current_num: str = "".join(current_num_list)
            print("\nYour Progress: " + current_num + "\n")
            return False
        else:
            print("Congrats! You got it right: " + str(generated_num))
            return True
    else:
        print("Your guess is not a number.")
        return False

def compare_nums(original_num: int, player_num: int, index: str) -> bool:
    if original_num > player_num:
        print("index " + index + ": is > than " + str(player_num))
        return False
    elif original_num < player_num:
        print("index " + index + ": is < than " + str(player_num))
        return False
    else:
        print("index " + index + ": is " + str(player_num))
        return True

start_game_print()
generated_num = generate_num()
generated_num_as_list = num_to_list(generated_num)


while True:
    user_input = input("")
    if user_input == "quit" or user_input == "no" or user_input == "stop":
        break
    else:
        if guess(user_input):
            continue_input = input("Continue? (yes/no)\n")
            if continue_input == "yes":
                generated_num = generate_num()
                generated_num_as_list = num_to_list(generated_num)
            else:
                break
