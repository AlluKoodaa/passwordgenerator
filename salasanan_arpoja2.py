###---AlluKoodaa---###

import random
import string

def generate_password(length: int, num: bool, punc: bool):
    punctuation ="!?=+-()#"
    numbers = "0123456789"
    letters = string.ascii_lowercase

    password = []
    if num:
        password.append(random.choice(numbers))
    if punc:
        password.append(random.choice(punctuation))
    while len(password) < length:
        password.append(random.choice(letters))
    random.shuffle(password)
    return "".join(password)

def main():
    length = int(input("Length of password: "))
    numerals = input("Numbers (Y/n): ")
    if numerals.casefold() == "y":
        num = True
    else:
        num = False
    punctuation = input("Punctuation (Y/n): ")
    if punctuation.casefold() == "y":
        punc = True
    else:
        punc = False
    
    password = generate_password(length, num, punc)
    print(password)
    answer = input("Try again (Y/n):  ")
    if answer.casefold() == "y":
        print("Reinitializing..")
        main()
    else:
        print("K thx bye")
        return None

main()

###---eof---###