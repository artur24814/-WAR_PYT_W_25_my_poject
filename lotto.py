from sys import exit
import random
def lotto():
    komputer_choice = []
    player_choice = []


    while True:
        try:
            while len(player_choice) != 6:
                x = int(input("wpisz 6 liczb : "))
                if x in player_choice:
                    print("już masz tą liczbe!")
                if x > 50 or x < 1:
                    print("Wpisz z zakresu od 1 do 49!")
                else:
                    player_choice.append(x)
            player_choice.sort()
            print(player_choice)
            while len(komputer_choice) != 6:
                y = random.randint(1, 49)
                if y in komputer_choice:
                    continue
                else:
                    komputer_choice.append(y)
            print(komputer_choice)
            goal = 0
            for i in range(6):
                if player_choice[i] == komputer_choice[i]:
                    goal +=1
            print(f"Trafiłesz {goal} razu")
            y = input("Chcesz jeszcze raz? Y/N")
            if "Y" in y:
                lotto()
            else:
                exit()



        except ValueError:
            print("Wpisz liczbę!")





lotto()

