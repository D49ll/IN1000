# Oppgave 2.1
svar = input("Kunne du tenke deg en brus?\n") #brukerinput

svar = svar.lower() #Konverterer string til små bokstaver

# Oppgave 2.2
if svar == "ja": #dersom bruker svarte ja
    print("Her har du en brus!")
elif svar == "nei": #dersom bruker svarte nei
    print("Den er grei")
else: #alle andre tilfeller
    print("Det forstod jeg ikke helt")