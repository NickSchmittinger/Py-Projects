import random
from typing import List

default_min_range = 1
default_max_range = 100

def start_game_print():
    print("Your guess will evaluate higher or lower for each index of the number.")
    print("For instance:\n The generated number is 152 and the player guesses 94.")
    print("The output will be ['is < than 9', 'is > than 4'].\n The actual number has 1 digit more than the guess.")

def generate_num(min: int = default_min_range, max: int = default_max_range) -> int:
    num: int = random.randint(min, max)
    print("A new number has been generated!\n It is between: " + str(min) + " and " + str(max))
    return num

def num_to_list(num: int) -> List[int]:
    return [int(x) for x in str(num)]

def guess(player_value: str) -> bool: 
    if player_value.isnumeric():
        guess_num_as_list: List[int] = [int(x) for x in str(player_value)]
        lists_compared_size = len(guess_num_as_list) - len(generated_num_as_list)

        if lists_compared_size > 0:
            print("Your guess was over the size of the number by " + str(abs(lists_compared_size)) + " digits.")
            return False
        elif len(lists_compared_size < 0):
            print("Your guess was under the size of the number by " + str(abs(lists_compared_size)) + " digits.")
            return False
        
        compared_list: List[str]
        for i in guess_num_as_list:
            compared_list.append(compare_nums(generated_num_as_list, guess_num_as_list, str(i)))
        if False in compared_list:
            return False
        else:
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
        print("index " + index + ": is = too " + str(player_num))
        return True

generated_num = generate_num()
generated_num_as_list = num_to_list(generated_num)

#while True:
    #user_input = input("")
    #if user_input == "quit" or user_input == "no":
        #print score and levels / nums completed
        #break
    #else:
        #takes in string, 
        #check input for potential non numeric value / actual guess,
        #returns a string:
        #"Not a number."
        #"Guess too low, attempts remaining(x)"
        #"Guess too high, attempts remaining(x)"
        #"Correct! Answer was: (guess), Continue?"
        #If continuing:
        #"There are (x) numbers left in this level.\n"
        #"Your guesses have been set too (x), good luck!"
        #If numbers left in level are 0:
        #"You completed the level! Want another?"
        #If yes: generate new number
        #"A new number has been generated between: min_value & max_value, good luck!"
        #If no / quit:
        #"Numbers Completed: (x)\n Total Guesses: (x)\n Final Score: (x)"
        #guess(user_input)