#Yofreilin
#2025-11-04

import random
def roll_die_simulation():

    num_rolls_str = "6"
    print(f"How many times would you like to roll a single sided die? {num_rolls_str}")
    num_rolls = int(num_rolls_str)
    for _ in range(num_rolls):
        roll_result = random.randint(1, 6)
        print(f"You rolled a {roll_result}!")
roll_die_simulation()