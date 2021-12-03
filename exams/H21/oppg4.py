#Oppgave 4a
class Onske:
    #NB Onske-objekter skal kun refereses til og brukes i Onskeliste-klassen
    def __init__(self, beskrivelse, antall, minPris):
        self._beskrivelse = beskrivelse
        self._antall = antall
        self._minPris = minPris

    def passer(self,maxPris):
        #Antar at returverdien skal være true/false basert på om gaven passer
        #da dette ikke var spesifisert i oppgavetekst
        if self._minPris > maxPris or self._antall == 0:
            return False
        return True

    def valgt(self):
        #Antar at dersom ønsket oppfylles så fjernes en iterasjon av ønsket
        self._antall -= 1
        return self._beskrivelse

    def __str__(self):
        return self._beskrivelse+' koster '+str(self._minPris)+'kr.'


#Oppgave 4b

class Onskeliste:

    def __init__(self):
        self._onskeliste = list()

    def nytt_onske(self,beskrivelse,antall,pris):
        #Oppretter et nytt ønske og legger det til i ønskelisten
        self._onskeliste.append(Onske(beskrivelse,antall,pris))
        

    def hent_onske(self,maxPris):
        #Returnerer en liste med tekststrenger, som representerer et ønske i ønskelisten.
            #For valgbare ønsker: Representasjon av objektet print()/str
            #For ikke valgbare ønsker: "Ikke valgbart onske"
        
        valgbareOnsker = list()
        for onske in self._onskeliste:
            if onske.passer(maxPris):
                valgbareOnsker.append(str(onske))
            else:
                valgbareOnsker.append('Ikke valgbart onske')

        return valgbareOnsker

    def onske_oppfylles(self,onske_valgt):
        #Metoden oppdaterer ønsket (heltall, index) og returnerer beskrivelsen av ønsket
        return self._onskeliste[onske_valgt].valgt()


#Oppgave 4c

class Gave:
    #NB: Gave-objekter skal kun referes til og brukes i Julegavekalenderklassen

    def __init__(self,beskrivelse,giver):
        self._beskrivelse = beskrivelse
        self._giver = giver

    def __str__(self):
        return self._beskrivelse+' blir oppfylt av '+self._giver+'.'

#Oppgave 4d

class Julegavekalender:
    
    def __init__(self,dager):
        self._julekalender = dict()

        if dager >= 25 and dager <= 31:
            for i in range(dager - 24):
                self._julekalender[25+i] = None
    
        elif dager >= 1 and dager <= 14:
            for dag in range(25,32):
                self._julekalender[dag] = None
            
            for i in range(dager):
                self._julekalender[i+1] = None
        else:
            print('Dato utenfor julegavekalenderens rekkevidde.')

    def ny_gave(self,beskrivelse,dag,giver):
        self._julekalender[dag] = Gave(beskrivelse,giver)

    def hent_dagens_gave(self,dag):
        if dag >= 25 and dag <= 31:
            mnd = 'desember'
        elif dag >= 1 and dag <= 14:
            mnd = 'januar'
        else:
            return 'Dato utenfor julekalenderens rekkevidde'
        
        if self._julekalender[dag] is None:
            beskrivelse = 'Ingen gave registrert på denne datoen.'
        else:
            beskrivelse = str(self._julekalender[dag])

        return str(dag)+'.'+mnd+', '+beskrivelse

    def hent_ant_dager(self):
        return len(self._julekalender)

#Oppgave 4e

class Julegavefikser:

    def __init__(self,antDager):
        self._nesteDag = 25 #Julegavekalenderen starter alltid fra og med 25desember.
        self._julekalender = Julegavekalender(antDager)
        self._onskeliste = Onskeliste()

    def les_onsker_fra_fil(self,fn):

        for linje in open(fn, 'r'):
            beskrivelse, antall, minPris = linje.rstrip('\n').split('; ')
            self._onskeliste.nytt_onske(beskrivelse,int(antall),int(minPris))

#Oppgave 4f

    def velg_gave(self):
        maxPris = int(input('Oppgi makspris for gaven: '))

        valgbareOnsker = self._onskeliste.hent_onske(maxPris)

        print('Tilgjengelige ønsker:')
        for i in range(len(valgbareOnsker)):
            print(f'{i+1}: {valgbareOnsker[i]}') #Øker i med 1 for finere utskrift

        valgtOnske = int(input('Oppgi indeksen for aktuelt ønske: '))

        beskrivelse = self._onskeliste.onske_oppfylles(valgtOnske-1) #Må trekke fra for riktig indeks iht visning

        dag = int(input('Hvilken dag ønskes gaven å gi? '))
        giver = input('Hvem er giver?: ')

        self._julekalender.ny_gave(beskrivelse,dag,giver)

    def ny_dag(self):
        gaveinfo = self._julekalender.hent_dagens_gave(self._nesteDag)
        self._nesteDag += 1

        if self._nesteDag > 31:
            self._nesteDag = 1

        return gaveinfo


def main():
    j1 = Julegavefikser(31)
    j1.les_onsker_fra_fil('test.txt')
    j1.velg_gave()
    print(j1.ny_dag())



main()

