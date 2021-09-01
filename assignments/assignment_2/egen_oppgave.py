'''
Oppgave 5: Egen oppgave

Del 1. 
Skriv din egen oppgavetekst til en oppgave som har med beslutninger å gjøre(if/else).

Del 2. 
Løs oppgaven! Du skal levere både oppgaveteksten og besvarelsen.
'''

'''
Oppgavetekst:
Skriv et prøveprogram som skal kontrollere om bruker har forstått pensum.
Prøven består av 5 spørsmål. For å bestå må man ha ingen feil.
'''

#Variabler
faults = 0

questions = [
    "Hva returnerer type(\"Hei\")? ",
    "Er a = 5 + \"2\" en gyldig operasjon? ", 
    "Hva er svaret til 5 * 5 + 2? ",
    "Er int(\"2.2\") en gyldig operasjon? ",
    "Er float(\"2.2\" en gyldig operasjon? "
]

answers = [
    "str",
    "nei",
    "27",
    "nei",
    "ja"
]

user_input = []

#Prøven
for i in range(0,len(questions)):
    answer = input(questions[i]).lower() #Hjelpevariabel for å sjekke om svar er riktig
    
    if answer == answers[i]: #Sjekker om svar er riktig ift fasit
        user_input.append(True)#Dersom riktig settes en boolsk verdi true
    else:#Dersom svaret er feil settes en boolsk verdi false
        user_input.append(False)
        faults += 1 #Oppdaterer antall feil

if all(user_input): #Dersom user_input kun består av boolsk true vil dette være sant
    print("Gratulerer, du alt riktig! Prøve bestått")
else:
    print(f"Beklager, du hadde {faults} feil. Prøve ikke bestått")