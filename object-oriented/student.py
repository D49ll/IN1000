class Student: #Klassenavn

    def __init__(self, navn): #Konstruktør (blir kalt hver gang et nytt objekt opprettes)
        self._ant_deltatt = 0 #Hver instans vil starte med 0 deltakere
                              #self. betyr at vi jobber på et spesielt objekt  
        self._navn = navn #_variabel brukes som navnekonvensjon som er "private", dvs skjult for programmet som bruker objektet. 
                          #Lokale variabler for klassen.
    
    def registrer(self): #Metode
        self._ant_deltatt += 1

    def hent_deltakelse(self): #Funksjonsmetode
        return self._ant_deltatt

    def hent_navn(self):
        return self._navn