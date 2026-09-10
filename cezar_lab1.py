ALFABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def verifica_cheie1(cheie):
    return 1 <= cheie <= 25


def verifica_text(text, cu_spatii=False):
    for litera in text:
        if cu_spatii and litera == " ":
            continue
        if not ("A" <= litera <= "Z" or "a" <= litera <= "z"):
            return False
    return True


def pregateste_mesaj(text):
    text = text.replace(" ", "")
    return text.upper()


def cezar(text, cheie, criptare=True, alfabet=ALFABET):
    rezultat = ""

    for litera in text:
        pozitie = alfabet.find(litera)

        if criptare:
            pozitie_noua = (pozitie + cheie) % 26
        else:
            pozitie_noua = (pozitie - cheie) % 26

        rezultat += alfabet[pozitie_noua]

    return rezultat


def construieste_alfabet(cheie2):
    alfabet_nou = ""

    for litera in cheie2.upper():
        if litera not in alfabet_nou:
            alfabet_nou += litera

    for litera in ALFABET:
        if litera not in alfabet_nou:
            alfabet_nou += litera

    return alfabet_nou


def citeste_cheie1():
    while True:
        try:
            cheie = int(input("Introdu cheia k (1-25): "))
            if verifica_cheie1(cheie):
                return cheie
            print("Cheia nu este corecta. Foloseste o valoare intre 1 si 25.")
        except ValueError:
            print("Cheia trebuie sa fie un numar intre 1 si 25.")


def citeste_cheie2():
    while True:
        cheie2 = input("Introdu cheia 2 (minimum 7 litere): ")

        if len(cheie2) < 7:
            print("Cheia 2 trebuie sa aiba cel putin 7 litere latine.")
            continue

        if not verifica_text(cheie2):
            print("Cheia 2 trebuie sa contina doar literele A-Z sau a-z.")
            continue

        return cheie2.upper()


def citeste_operatie():
    while True:
        operatie = input("Alege operatia (1 - criptare, 2 - decriptare): ")
        if operatie in ("1", "2"):
            return operatie
        print("Alege 1 pentru criptare sau 2 pentru decriptare.")


def lucreaza_cezar():
    operatie = citeste_operatie()
    cheie = citeste_cheie1()

    if operatie == "1":
        mesaj = input("Introdu mesajul: ")
        if not verifica_text(mesaj, cu_spatii=True):
            print("Mesajul poate contine doar literele A-Z, a-z si spatii.")
            return

        mesaj = pregateste_mesaj(mesaj)
        if mesaj == "":
            print("Mesajul nu poate fi gol.")
            return

        rezultat = cezar(mesaj, cheie, True)
        print("Criptograma:", rezultat)
    else:
        criptograma = input("Introdu criptograma: ")
        if not verifica_text(criptograma):
            print("Criptograma poate contine doar literele A-Z sau a-z.")
            return

        criptograma = criptograma.upper()
        if criptograma == "":
            print("Criptograma nu poate fi goala.")
            return

        rezultat = cezar(criptograma, cheie, False)
        print("Mesajul decriptat:", rezultat)


def lucreaza_cezar_plus():
    operatie = citeste_operatie()
    cheie1 = citeste_cheie1()
    cheie2 = citeste_cheie2()
    alfabet_nou = construieste_alfabet(cheie2)

    print("Alfabetul nou:", alfabet_nou)

    if operatie == "1":
        mesaj = input("Introdu mesajul: ")
        if not verifica_text(mesaj, cu_spatii=True):
            print("Mesajul poate contine doar literele A-Z, a-z si spatii.")
            return

        mesaj = pregateste_mesaj(mesaj)
        if mesaj == "":
            print("Mesajul nu poate fi gol.")
            return

        rezultat = cezar(mesaj, cheie1, True, alfabet_nou)
        print("Criptograma:", rezultat)
    else:
        criptograma = input("Introdu criptograma: ")
        if not verifica_text(criptograma):
            print("Criptograma poate contine doar literele A-Z sau a-z.")
            return

        criptograma = criptograma.upper()
        if criptograma == "":
            print("Criptograma nu poate fi goala.")
            return

        rezultat = cezar(criptograma, cheie1, False, alfabet_nou)
        print("Mesajul decriptat:", rezultat)


def main():
    while True:
        print("\n--- CIFRUL CEZAR ---")
        print("1. Cezar")
        print("2. Cezar + permutare")
        print("0. Iesire")

        alegere = input("Alege varianta: ")

        if alegere == "1":
            lucreaza_cezar()
        elif alegere == "2":
            lucreaza_cezar_plus()
        elif alegere == "0":
            print("Program terminat.")
            break
        else:
            print("Optiune invalida. Alege 0, 1 sau 2.")


if __name__ == "__main__":
    main()
