import random

def geme1():
    komputer_choise = random.randint(1, 100)
    while True:
        try:
            user_number = int(input("Guess the number: "))
            if user_number < komputer_choise:
                print("To small!")
            elif user_number > komputer_choise:
                print("To big!")
            elif user_number == komputer_choise:
                return print("You win!")
        except Exception:
            print("It's not a number!")

geme1()
