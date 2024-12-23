import random
import decimal

#This file was started at 4:00 AM.
#I will pick it back up later in the day.

min_range = 0.0
max_range = 100.0


def generate(precision=100):
    with decimal.localcontext() as ctx:
        ctx.prec = precision
        return decimal.Decimal(random.uniform(min_range,max_range))

def guess(value: str) -> bool: 
    # print("You got the entire number correct!\n")
    # confirm = input("Ready for the next number? (yes/no) ")

    # print("Good job!")
    # guess_num = input("" + "\n ")
    if value.isnumeric():
        #check if num is correct
        return True
    print("Not a number (1-9). ")
    return False

random_num = generate()
print("A new number has been generated between: " + str(min_range) + " & " + str(max_range))
num_str_list = str(random_num).split(".", 1)

num_whole = float(num_str_list[0])
num_dec = float(num_str_list[1])

num_whole_count = len(num_str_list[0])
num_dec_count = len(num_str_list[1])

while True:
    user_input = input("")
    if user_input == "quit" or user_input == "no":
        #print score and levels / nums completed
        break
    else:
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
        guess(user_input)