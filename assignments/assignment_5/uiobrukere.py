'''
Oppgave 2: UiO-brukere
'''

def lag_brukernavn(navn):
    fornavn, etternavn = navn.lower().split()
    return fornavn+etternavn[0]

def lag_epost(brukernavn, suffix):
    return brukernavn+'@'+suffix

def skriv_ut_eposter(brukerbok):
    for key, val in brukerbok.items():
        print(lag_epost(key,val))

def main():
    ordbok = dict()

    inp = input("Skriv:\ni for å legge til bruker\np for å printe epost\ns for å avslutte. ")
    while inp != "s":
        print()

        if inp == "i":
            navn = input("Skriv et navn: ")
            suffix = input("Skriv en suffix: ")
            bruker_navn = lag_brukernavn(navn)
            ordbok[bruker_navn] = suffix

        elif inp == "p":
            skriv_ut_eposter(ordbok)

        print()
        inp = input("Skriv:\ni for å legge til bruker\np for å printe epost\ns for å avslutte. ")

main()