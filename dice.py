#x D y + z
import random


def dice(x):
    lista_kostek = ['3', '4', '6', '8', '10', '12', '20', '100']
    lista = []
    lista1 = x.split("+")

    if len(lista1) != 2:
        lista1 = x.split("-")

        if len(lista1) == 2:
            y = lista1[0]
            mod = int(lista1[1])
            z = y.split("D")

            if len(z) == 1:
                print("one throw")
                type_dice = z[1]
                if type_dice not in lista_kostek:
                    print("such type of dice does not exist!")
                    return print("invalid format!")
                else:
                    print(f"Type of dice D{type_dice}")
                result = random.randint(1, int(type_dice)) - mod
                return f'result = {result}'


            elif len(z) == 2:
                throw = int(z[0])
                print(f"throw a dice : {throw}")
                type_dice = z[1]
                if type_dice not in lista_kostek:
                    print("such type of dice does not exist!")
                    return print("invalid format!")
                else:
                    print(f"Type of dice D{type_dice}")
                result = throw * (random.randint(1, int(type_dice))) - mod
                return f'result = {result}'
            else:
                return print("invalid format!")
        else:
            return print("invalid format!")
    elif len(lista1) == 2:
        y = lista1[0]
        mod = int(lista1[1])
        z = y.split("D")

        if len(z) == 1:
            print("one throw")
            type_dice = z[1]
            if type_dice not in lista_kostek:
                return print("such type of dice does not exist!")
            else:
                print(f"Type of dice D{type_dice}")
            result = random.randint(1, int(type_dice)) + mod
            return f'result = {result}'

        elif len(z) == 2:
            throw = int(z[0])
            print(f"throw a dice : {throw}")
            type_dice = z[1]
            if type_dice not in lista_kostek:
                return print("such type of dice does not exist!")
            else:
                print(f"Type of dice D{type_dice}")
            result = throw * (random.randint(1, int(type_dice))) + mod
            return f'result = {result}'
        else:
            return print("invalid format!")

    elif lista1 != 2:
      return print("invalid format!")






print(dice("2D20-10"))