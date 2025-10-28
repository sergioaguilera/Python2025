"""Exercise: Roll 2 dices
Needs a loop 
    Ask: roll the dice?
        if say y
            generate  two random numbers
            print them
        if say n
            print thank you
Terminate the program
"""
import random


def dice_game():
    execute = True
    while execute:
        choice = input("Do you wanna you the dice (y/n)").lower()
        if choice == "y":
            n1 = random.randint(1, 6)
            n2 = random.randint(1, 6)
            print(n1, n2)
            if n1 > n2:
                print(f"""{n1} its the winner""")
            elif n1 == n2:
                print("They have the same value")
            else:
                print(f"""{n2} its the winner""")

        elif choice == "n":
            print("thanks for using the app")
            execute = False


dice_game()
print("""************************************************
        Created by: Sergio.aaguilera@gmail.com
        October 2025.""")
