'''Oppgave 5: Egen oppgave

1.  Skriv oppgavetekst til en oppgave som handler om lister eller ordbøker

    Skriv et quizprogram som har 2 ulike temaer. For hvert tema finnes det
    3 ulike spørsmål. Programmet skal skrive ut hvor mange riktige svar
    brukeren har etter quizen er ferdig. Brukeren velger selv tema.

'''

def convert_input(svar):
    '''
    Konverterer input til å starte med stor forbokstav og resten små
    Fungerer kun på en streng uten mellomrom.
        input = KARI
        output = Kari
    '''
    list_of_char = list(svar)

    for i in range(len(list_of_char)):
        if i == 0:
            list_of_char[0] = list_of_char[0].upper()
        else:
            list_of_char[i] = list_of_char[i].lower()
    
    svar = "".join(list_of_char)

    return svar

# Definerer temaer med tilhørende svar
tema = {
    "Hovedsteder i verden"
    :{"Norge":"Oslo", "Tyskland":"Berlin","Spania":"Madrid"},
    "Kontinenter i verden"
    :{"Afghanistan":"Asia", "Australia":"Oseania","Hviterussland":"Europa"}
    }

# Definerer hjelpevariabler og dict dersom feil svar
antall_feil = 0
feil_svar = {}

# Skriver til terminal som opplyser hvilke temavalg bruker har
print("Velkommen til quiz! Du kan velge mellom følgende temaer:")
for i, key in enumerate(tema):
    print(f"For temaet \"{key}\", skriv {i+1} terminalen")
    
# Basert på brukerinput blir temaet satt
while True:
    tema_valg = int(input("Hvilket tema ønsker du? "))

    if tema_valg == 1:
        valg = "Hovedsteder i verden"
        sporsmal = "hovedstaden"
        break

    elif tema_valg == 2:
        valg = "Kontinenter i verden"
        sporsmal = "kontinentet"
        break
    else:
        print(f"Du tastet {tema_valg}, som er et ugyldig valg. Prøv igjen.")


# Quiz settes igang, temaet er basert på brukerinput
print()
print(f"Du valgte temaet: {valg}. Lykke til!")
for key, val in tema[valg].items():
    svar = input(f"Hva er {sporsmal} til {key}? ")
    print(svar)
    svar = convert_input(svar)

    # Dersom bruker svarer feil lagres feil svar
    if svar != val:
        antall_feil += 1
        feil_svar[key] = svar

# Resultatet kommuniseres til bruker
if antall_feil:
    print()
    print(f"Du hadde dessverre {antall_feil} feil!")
    for key, value in feil_svar.items():
        print(f"Du sa at {sporsmal} til {key} var {value}.")
    print()
    print("Bedre lykke neste gang!")
else:
    print(f"Gratulerer, du hadde {antall_feil} feil!")