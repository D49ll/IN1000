'''Oppgave 4: Matplan

1.  Lag en ordbok hvor hver nøkkelverdi er navnet til en beboer,
    og innholdsverdien er en liste med tre måltider. Måltidende
    skal være henholdsvis frokost, lunsj og middag.
    
'''

#Definerer matplanen til beboere
maltider = {"Kari":{"Frokost":"Brød","Lunsj":"Egg","Middag":"Pylsa"},
            "Ola":{"Frokost":"Knekkis","Lunsj":"Pasta","Middag":"Pylsa med saus"},
            "Espen":{"Frokost":"Avacado","Lunsj":"Vin","Middag":"Pylsa med ketchup"},
}

'''
2.  Lag en prosedyre som skriver ut navene til alle beboere og spør brukeren om å
    skrive navnet til en beboer i terminalen.
'''

def print_maltider(maltider):
    '''
    Denne funksjonen oppgir hvem som bor i boligkomplekset. Deretter gir
    den bruker mulighet å få vite matplanen til ønsket bruker ved og skrive
    inn navnet på brukeren.

    Programmer kjører så lenge bruker ønsker. Bruker avslutter programmet med å 
    skrive exit i terminalen
    '''

    flag = True

    print(f"I dette boligkomplekset bor:")
    for k in maltider:
        print(k)

    while flag:
        beboer = input("\nHvem ønsker du å vite matplanen til?\nSkriv \"exit\" for å avslutte.\n")
        beboer = convert_input(beboer)

        if beboer == "Exit":
            print("Avslutter..")
            flag = False
        elif beboer in maltider:
            print()
            for k, v in maltider[beboer].items():
                print(f"{beboer} spiser {v} til {k}")
        else:
            print(f"Ingen som heter {beboer}")

def convert_input(beboer):
    '''
    Konverterer input til å starte med stor forbokstav og resten små
        input = KARI
        output = Kari
    '''
    list_of_char = list(beboer)
    
    for i in range(len(list_of_char)):
        if i == 0:
            list_of_char[0] = list_of_char[0].upper()
        else:
            list_of_char[i] = list_of_char[i].lower()
    
    beboer = "".join(list_of_char)

    return beboer

#Prosedyrekallet
print_maltider(maltider)


'''
3.  Hvilken type samling (liste, mengde, ordbok) ville du brukt for å representere 
    hver av de følgende eksemplene på data. Skriv litt om hvorfor.

    a. Brukernavn på alle IN1000 studenter
'''