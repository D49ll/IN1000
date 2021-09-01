'''
Oppgave 1: Utskriftsprosedyre

Del 1.
Lag et program som kommuniserer med brukeren slik at det tar inn et navn og et bosted fra terminalen. 

Del 2.
Flytt koden som leser inn informasjon og skriver ut en hilsen til en egen prosedyre.
Kall denne prosedyren 3 ganger slik at du får lest inn og skrevet ut informasjon om 3 personer. 
'''

#Del 1 og 2.
def utskriftsfunksjon():
    #Brukerinput
    navn = input("Skriv inn navnet ditt: ")
    bosted = input("Hvor kommer du fra? ")

    #Printer til terminal
    print(f"\nHei, {navn}! Du er fra {bosted}\n")

for i in range (3): #Utføres 3 ganger
    utskriftsfunksjon() #Prosedyrekall