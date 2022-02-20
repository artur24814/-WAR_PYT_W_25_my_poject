import random

komputer_point = 0
gemer_point = 0
print("Type of dices: 3, 4, 6, 8, 10, 12, 20, 100")
list_of_dice = ['3', '4', '6', '8', '10', '12', '20', '100']
input("Ready? > ")

while True:

    type_dice_g = []
    while len(type_dice_g) != 2:
        geme_dice = input("Choose type of dice > ")
        if geme_dice not in list_of_dice:
            print("such type of dice does not exist!")
        else:
            type_dice_g.append(geme_dice)
    y1 = int(type_dice_g[0])
    y2 = int(type_dice_g[1])
    x1 = int(list_of_dice[random.randint(0, 7)])
    print(f"komputer choose : {x1}")
    x2 = int(list_of_dice[random.randint(0, 7)])
    print(f"komputer choose : {x2}")
    x = int(random.randint(1, x1)) + int(random.randint(1, x2))
    komputer_point += x
    y = int(random.randint(1, y1)) + int(random.randint(1, y2))
    gemer_point += y
    if x == 7:
        komputer_point = komputer_point // 7
    if x == 11:
        komputer_point = komputer_point * 11
    if y == 7:
        gemer_point = gemer_point // 7
    if y == 11:
        gemer_point = gemer_point * 11
    print(f"gamer point : {gemer_point}")
    print(f"komputer point : {komputer_point}")
    if komputer_point > 2001 or gemer_point > 2001:
        break

