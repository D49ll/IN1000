class Student:

    def __init__(self, brukernavn):
        self._brukernavn = brukernavn
        self._emner = []

    def hentBrukernavn(self):
        return self._brukernavn


class Emne:
    def __init__(self,emnekode):
        self._emnekode = emnekode
        self._aktiviteter = []

    def leggTilAktivitet(self,aktivitet):
        self._aktiviteter.append(aktivitet)

    def emne(self):
        return self._emnekode

class Dato:

    def __init__(self, dag,maaned,aar):
        self._dag = dag
        self._maaned = maaned
        self._aar = aar

    def absoluttDato(self):
        dag = str(self._dag)
        maaned = str(self._maaned)
        aar = str(self._aar)

        if len(dag)<2:
            dag = '0'+dag

        if len(maaned)<2:
            maaned ='0'+maaned
        
        if len(aar)<2:
            aar = '0'+aar

        return int(dag+maaned+aar)

    def __str__(self):
        maaneder = {9:'September',10:'Oktober',11:'November',12:'Desember'}

        return str(self._dag)+'. '+maaneder[self._maaned]+' 20'+str(self._aar)

class Aktivitet:

    def __init__(self,emne,dato,aktivitetsnummer):
        self._emne = emne
        self._dato = dato
        self._aktivitetsnummer = aktivitetsnummer

        self._studentweb = []
        self._oppmote = []

    def leggTilRegistertStudent(self, student):
        self._studentweb.append(student)

    def registrerOppmote(self,student):
        self._oppmote.append(student)

    def skrivUtOppmoteStudenter(self):
        for student in self._oppmote:
            print(student.hentBrukernavn())
    
    def absoluttDato(self):
        return self._dato.absoluttDato()

    def oppmote(self):
        return len(self._oppmote)

    def __str__(self):

        return str(self._emne.emne())+','+str(self._aktivitetsnummer)+','+str(self.oppmote)


class Undervisningsadministrasjon:
    def __init__(self):
        self._emner = dict()
        self._datoer = dict()
        self._studenter = dict()

    def lesFraFil(self,filnavn):
        f = open(filnavn)