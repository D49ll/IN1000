class Emne:
    def __init__(self,emnekode, obliger, rettere, studenter):
        self._emnekode = emnekode #int
        self._studenter = studenter #ordbok med Student-objekter
        self._rettere = rettere #liste med Retter-objekter
        self._obliger = dict() #tom ordbok

    def _emneMeny(self):
        print(f'Meny for {self._emnekode}')
        print('O: Ny oblig')
        print('F: Frist ute, start retting')
        print('L: Lag eksamensliste')


    def administrer(self):
        '''
        Skriver ut emnekoden og meny på terminalen før den ber om kommando. Lovlige kommandoer -> O,F,L,A
        '''
        self._emneMeny()
        brukerInput = input('Skriv ønsket kommando: ').strip().upper()
        while brukerInput != 'A':
            if brukerInput == 'O':
                self._opprettOblig()
            elif brukerInput == 'F':
                self._startRetting()
            elif brukerInput == 'L':
                self._skrivEksamensListe()
            else:
                print('feil input')

            brukerInput = input('Skriv ønsket kommando: ').strip().upper()


class Student:
    def __init__(self,brukernavn,fultNavn):
        self._brukernavn = brukernavn
        self._fultNavn = fultNavn
        self._obliger = dict()

    def registrer(self,obligId,resultat):
        self._obliger[obligId] = resultat

    def altGodkjent(self,antObliger):
        #Dersom en oblig er underkjent
        for obliger in self._obliger.values():
            if obliger < 1:
                return False
        
        #Dersom student levert og bestått alle obliger
        if len(self._obliger) == antObliger:
            return True
        
        #Dersom studenten ikke har levert alle obliger
        return False


class Retter:
    def __init__(self, retterBrukernavn):
        self._retter = retterBrukernavn

    def vurder(self,filnavn):
        return 1

    
class Oblig:
    def __init__(self, obligId,frist):
        self._obligId = obligId
        self._frist = frist
        self._rettet = False

    def klarForRetting(self,dato):
        if int(self._frist)<int(dato) and not self._rettet:
            return True
        return False

    def hentBesvarelse(self,filnavn):
        for linje in open(filnavn):
            studentNavn, *obliger = linje.split(' ')

            for oblig in obliger:

        


