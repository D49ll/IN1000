class Oblig:
    def __init__(self,obligId,frist):
        self._obligId = obligId
        self._frist = frist
        self._rettet = False

    def klarForRetting(self,dato):
        if dato > self._frist and not self._rettet:
            return True
        else:
            return False

    def hentBesvarelser(self):
        besvarelser = dict()
        for linje in open(self._obligId+'.txt'):
            linje = linje.split()
            if len(linje) > 1:
                besvarelser[linje[0]] = linje[1]
        return besvarelser    

    def fordelRetting(self, besvarelser, rettere):
        antRetter = len(rettere)
        resultat = dict()
        i = 0
        for student, fn in besvarelser.items():
            resultat[student] = rettere[i].vurder(fn)
            i = (i + 1) % antRetter

        self._rettet = True
        return resultat

    def hentObligId(self):
        return self._obligId

class Emne:
    def __init__(self, emnekode,studenter,rettere):
        self._emnekode = emnekode
        self._studenter = studenter
        self._rettere = rettere
        self._antObliger = 0
        self._obliger = list()

    def administer(self):
        print(f'Emnekode for faget: {self._emnekode}')

        print('Oppgi ønsket kommando av følgende meny:')
        print('O: Ny oblig')
        print('F: Frist ute, start retting')
        print('L: Lag eksamensliste')
        print('A: Avslutt')

        brukerinput = self._formatertInput('Oppgi ønsket input: ')
        while brukerinput != 'A':
            if brukerinput == 'O':
                self._opprettOblig()
            elif brukerinput == 'F':
                self._startRetting()
            elif brukerinput == 'L':
                self._skrivEksamensListe()
            else:
                print('Feil format! prøv igjen')

            brukerinput = self._formatertInput('Oppgi ønsket input: ')

    def _formatertInput(self,tekst):
        brukerinput = input(tekst)
        return brukerinput.strip().upper()

    def _opprettOblig(self):
        obligId = 'oblig'+str(self._antObliger)
        self._antObliger += 1
        frist = int(input('Oppgi oblig frist [ååmmdd]: '))
        self._obliger.append(Oblig(obligId,frist))
        print(f'{obligId} opprettet')

    def _startRetting(self):
        dato = int(input('Oppgi dagens dato [ååmmdd]: '))

        for oblig in self._obliger.values():
            if oblig.klarForRetting(dato):
                besvarelser = oblig.hentBesvarelser()
                resultat = oblig.fordelRettere(besvarelser,self._rettere)
                obligID = oblig.hentObligId()

                for studentID, result in resultat.items():
                    self._studenter[studentID].registrer(obligID,result)

    def _skrivEksamensListe(self):
        eksamensliste = list()
        for k,v in self._studenter.items():
            if v.altGodkjent(self._antObliger):
                eksamensliste.append(k)

        print('Studenter som kan ta eksamen er:')
        for student in eksamensliste:
            print(student)
        

class Student:
    def __init__(self,brukernavn,navn):
        self._bNavn = brukernavn
        self._fNavn = navn
        self._resultat = dict()

    def register(self, obligId,resultat):
        self._resultat[obligId] = resultat
    
    def altGodkjent(self,antObliger):
        if len(self._resultat < antObliger):
            return False

        for r in self._resultat:
            if r != 1:
                return False

        return True

class Retter:
    def __init__(self,rbrukernavn):
        self._bNavn = rbrukernavn

    def vurder(self,fn):
        return 1
    






e = Emne('IN2000',10,10)

#e.administer()

oblig1 = Oblig('oblig1',15)

print(oblig1.hentBesvarelser())

