'''
author =
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
         '''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
         '''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.''']

uzivatele = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

jmeno = input("Zadej přihlašovací jméno: ")
heslo = input("Zadej heslo: ")
oddelovac = "-" * 40

if uzivatele.get(jmeno):
    if uzivatele[jmeno] == heslo:
        print(oddelovac)
        print("Vítej v programu,", jmeno.title())  # uvitani + zajisteni, aby melo jmeno velke pismeno
        print("Máme 3 texty, které je možné analyzovat")
        print(oddelovac)
        zadani = input("Vyber číslo textu, který chceš analyzovat (min 1, max 3): ")
        if zadani.isalpha():
            print("Špatné zadání, zadej číslo")
        elif 1 <= int(zadani) <= 3:

            text_list = TEXTS[int(zadani) - 1].split()  # prevadim text do listu a upravuji index dle volby uzivatele

            text = []  # odstranuji z textu carky a tecky
            for slovo in text_list:
                text.append(slovo.strip(",."))

            pocet_slov = len(text)
            print(f"V textu je celkem {pocet_slov} slov.")
            pocet_velky_pocatek = 0
            pocet_velka_pismena = 0
            pocet_mala_pismena = 0
            pocet_cisel = 0
            soucet_cisel = 0

            for slovo in text:
                if slovo.istitle():
                    pocet_velky_pocatek += 1

            print(f"V textu je celkem {pocet_velky_pocatek} slov začínajících velkým písmenem.")

            for slovo in text:
                if slovo.isupper() and slovo.isalpha():
                    pocet_velka_pismena += 1
            print(f"V textu je celkem {pocet_velka_pismena} slov psaných velkými písmeny.")

            for slovo in text:
                if slovo.islower():
                    pocet_mala_pismena += 1
            print(f"V textu je celkem {pocet_mala_pismena} slov psaných malými písmeny.")

            for slovo in text:
                if slovo.isdigit():
                    pocet_cisel += 1
                    soucet_cisel += int(slovo)
            print(f"V textu je celkem {pocet_cisel} čísel.")
            print(f"Součet všech čísel v textu je {soucet_cisel}.")

            delky_slov = []  # prazdny seznam, do ktereho se budou ukladat cisla odpovidajici delce daneho slova ve vybranem textu

            for slovo in text:
                delky_slov.append(len(slovo))

            delky_slov.sort()

            slovnik = {}  # prazdny slovnik, do ktereho budu prirazovat cetnost slova o dane delce

            for i in delky_slov:
                slovnik[i] = slovnik.get(i, 0) + 1

            maximalni_vyskyt = max(list(
                slovnik.values()))  # zjistim max.hodnotu nejcastejsiho slova (pouziji pro zarovnani vypisu cetnosti pomoci hvezdicek).

            OCCURENCES = "ČETNOST"

            print(oddelovac)

            print(f"LEN|{OCCURENCES:^{maximalni_vyskyt + 2}s} |Č.")

            print(oddelovac)

            for i in slovnik:
                hvezdicky = "*" * slovnik[i]
                print(f"{i:3d}|{hvezdicky:<{maximalni_vyskyt + 2}s} |{slovnik[i]:>d}")

        else:
            print("Zadal jsi neexistující číslo textu")

    else:
        print("Špatné heslo")
else:
    print("Neexistujicí uživatel")
