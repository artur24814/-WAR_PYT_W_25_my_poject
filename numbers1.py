
def licz():
    print("Pomuśl liczbę od 0 do 1000, a ja ją zgadnię w max. 10 próbach")
    min = 0
    max = 1000
    koniec = False
    input("Gotowy?")

    while not koniec:
        guess = int((max - min) / 2) + min
        print(f"Zgaduje: {guess}")
        print("""
        Pobierz odpowiedż ze zestawu:
        -za dużo,
        -za mało,
        -zgadłesz
        """)
        y = input("Zgadłesz? Y/N > ")
        if "Y" in y:
            print("Wygrałem!")
            koniec = True
        else:
            x = input("za dużo? Y/N > ")
            if "Y" in x:
                max = guess
            else:
                z = input("za mało? Y/N > ")
                if "Y" in z:
                    min = guess
                else:
                    print("nie oszukuj!")


licz()
