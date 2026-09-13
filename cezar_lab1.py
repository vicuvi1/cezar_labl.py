alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def verifica_text(text):
    for litera in text:
        if litera != " " and litera.upper() not in alfabet:
            return False
    return True


def cezar(text, k, optiune, alfabet_curent=alfabet):
    rezultat = ""

    for litera in text:
        pozitie = alfabet_curent.index(litera)

        if optiune == "c":
            pozitie = (pozitie + k) % 26
        else:
            pozitie = (pozitie - k) % 26

        rezultat += alfabet_curent[pozitie]

    return rezultat


def alfabet_permutat(cheie):
    nou = ""

    for litera in cheie.upper() + alfabet:
        if litera not in nou:
            nou += litera

    return nou


def citeste_cheie():
    while True:
        try:
            k = int(input("introdu cheia k (1-25): "))

            if 1 <= k <= 25:
                return k

        except ValueError:
            pass

        print("cheia trebuie sa fie intre 1 si 25.")


def citeste_cheie2():
    while True:
        cheie = input("introdu cheia 2 (minim 7 litere): ")

        if len(cheie) >= 7 and verifica_text(cheie):
            return cheie

        print("introdu cel putin 7 litere a-z.")


varianta = input("1 - cezar, 2 - cezar + permutare: ")
optiune = input("c - criptare, d - decriptare: ")

if varianta == "1":
    k = citeste_cheie()
    text = input("introdu textul: ")

    if verifica_text(text):
        text = text.replace(" ", "").upper()

        if optiune == "c" or optiune == "d":
            print("rezultat:", cezar(text, k, optiune))
        else:
            print("optiune invalida.")
    else:
        print("sunt permise doar literele a-z si spatii.")

elif varianta == "2":
    k = citeste_cheie()
    cheie2 = citeste_cheie2()

    alfabet_nou = alfabet_permutat(cheie2)
    print("alfabetul nou:", alfabet_nou)

    text = input("introdu textul: ")

    if verifica_text(text):
        text = text.replace(" ", "").upper()

        if optiune == "c" or optiune == "d":
            print("rezultat:", cezar(text, k, optiune, alfabet_nou))
        else:
            print("optiune invalida.")
    else:
        print("sunt permise doar literele a-z si spatii.")

else:
    print("varianta invalida.")
