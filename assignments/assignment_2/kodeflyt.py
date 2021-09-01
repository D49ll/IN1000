''''
Oppgave 3: Kodeflyt

Du skal forklare programflyten til et program, det vil si i hvilken rekkefølge
de forskjelligelinjene utføres når vi kjører programmet. Du skalgjøre dette 
ved å skrive tall foran linjene iprogrammet. Tallene beskriver i hvilken r
ekkefølgeprogramsetningene utføres, slik at 1 erden første setningen som 
utføres, 2 er den neste,og så videre. 
'''

def print_prosa():  #Her defineres en prosedyre til senere bruk. 
                    #Den brukes ved prosedyrekall i koden.

   1 print("Melding til alle gaardeiere: ") #Ved et prosedyrekall skrives 
                                            #dette til terminalen

   2 print("Antall dyr paa gaarden: ")      #Etterfølgt av dette


1 antall_dyr = 4    #Her tilegnes variablenen, antall_dyr, heltallet 4

2 print_prosa()     #Her utføres et prosedyrekall som kjøres prosedyren.
                    #Dette kallet vil kjøre 1 og 2 i prosedyrekroppen.

3 print(antall_dyr) #Deretter printes variablen, antall_dyr, til terminalen.

4 antall_nye_dyr = int(input("Hvor mange nye dyr kommer til gaarden: "))
                    #Her skrives str argumentet i input til terminalen
                    #Dersom bruker skriver inn et heltall blir det kastet fra
                    #str til en int. Dette heltallet tilegnes antall_nye_dyr.
                    #Dersom input ikke er et heltall får man en feilmelding.
                    #Antar videre at antall_nye_dyr = 8. 

5 antall_dyr = antall_dyr + antall_nye_dyr #Her summers antall_dyr med 
                                           #antall_nye_dyr gitt fra bruker.

6 print_prosa() #Her utføres et prosedyrekall som kjøres prosedyren.
                #Dette kallet vil kjøre 1 og 2 i prosedyrekroppen.

7 print(antall_dyr)#Deretter printes oppdatert antall_dyr til terminalen

8 if antall_dyr > 12:#Sjekker om antall_dyr er større enn 12, som er usant.
    print("Det er mer enn et dusin dyr paa gaarden!")#Blir ikke evaluert.
                                                    
9 elif antall_dyr == 12:#Sjekker så om antall_dyr er lik 12, som er usant.
    print("Det er ett dusin dyr paa gaarden! ")#Blir ikke dette evaluert

10 else:#Da if og elif sjekkene er usanne, vil python utføre else
    print("Det er mindre enn ett dusin dyr paa gaarden! ")#Printer dette
