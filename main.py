import math

from string import hexdigits
from random import random

def create_hex_code(length):
    code = ""
    for x in range(length):
        code += hexdigits[get_rand_num(len(hexdigits))]
    return code

def get_rand_num(length):
    rand = random()
    return math.floor(length * rand)

running = True
list_of_codes = []

while running:
    try:
        entry = input("Please enter the length of the hex string to generate or codes to see generated codes:\n")

        if entry == "codes" or entry == "code":
            print(f"\nAll generated codes:")
            for code in list_of_codes:
                print(f"{code}")
        elif int(entry):
            code = create_hex_code(int(entry))
            list_of_codes.append(code)
            
            print(f"Your random hex code of {int(entry)} digits is: {code}.")

        print("Press any key to continue, or type q to quit.")
        
        check_q = input("")
        if check_q == "q" or check_q == "quit":
            quit()
        else:
            continue

    except ValueError:
        print("Incorrect input, please try again.")

