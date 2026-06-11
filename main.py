import math
import json

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
        entry = input("Please enter the length of the hex string to generate, codes to see generated codes, or print to push the codes to a file:\n")

        if entry == "codes" or entry == "code":
            print(f"All generated codes:")
            for code in list_of_codes:
                print(f"{code}")
        elif entry == "print":
            print("Adding to file: codes.json...")
            f = open("codes.json", "w")
            codes = {}
            for i in range(len(list_of_codes)):
                codes[i] = list_of_codes[i]
            json_str = json.dumps(codes)
            f.write(json_str)
            f.close()
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

