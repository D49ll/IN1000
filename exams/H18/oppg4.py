# Oppgave4a

class Rett:
    def __init__(self,navn,pris,innhold=list()):
        self._navn = navn
        self._pris = pris
        self._innholdsstoffer = innhold
        
    def sjekkInnholdOk(self,innholdsstoffer):
        for stoff in innholdsstoffer:
            if stoff in self._innholdsstoffer:
                return False
        return True

    def rettNavn(self):
        return self._navn

    def __str__(self):
        if len(self._innholdsstoffer) < 1:
            return self._navn+' koster '+str(self._pris)+'kr og har ingen info om innholdsstoffer'
        else:
            return self._navn+' koster '+str(self._pris)+'kr og inneholder '+str(self._innholdsstoffer)


#Oppgave4b

class Kategori:
    def __init__(self, kategorinavn, retter):
        self._kategori = kategorinavn
        self._retter = retter

    def hentOkRetter(self,innholdsstoffer):
        ok_retter = []

        for rett in self._retter:
            if rett.sjekkInnholdOk(innholdsstoffer):
                ok_retter.append(rett)
        
        return ok_retter

class Meny:
    def __init__(self,kategorinavn):
        self._meny = dict()

        for kategori in kategorinavn:
            self._meny[kategori] = self._LesKategoriFil(kategori+'.txt')

    def _lesKategoriFil(self,fn):
        pass

    def hentRedusertMeny(self,innholdsstoffer):
        redusert_meny = dict()

        for k,v in self._meny.items():
            ok_retter = v.hentOkRetter(innholdsstoffer)
            if len(ok_retter)>0:
                redusert_meny[k] = ok_retter

        return redusert_meny

class Kunde:
    def __init__(self,tlf,innholdsstoffer = list()):
        self._tlf = tlf
        self._innholdsstoffer = innholdsstoffer 

    def velgRetter(self,full_meny):
        redusert_meny = full_meny.hentRedusertMeny(self._innholdsstoffer)
        bestilling = list()
        for k, v in redusert_meny.items():
            print(f'Kategori {k} innholder følgende retter: {v}')
            valgt_rett = input('Velg en rett ved å skrive navnet eller press enter for å fortsette: ')
            
            while valgt_rett != '\n':
                if valgt_rett in v:
                    bestilling.append(valgt_rett)
                else:
                    print('feil input, prøv igjen.')
                
                valgt_rett = input('Velg en rett ved å skrive navnet eller press enter for å fortsette: ')
        
        return bestilling


class TakeAway:
    def __init__(self,kategorinavn,kundefil):
        self._meny = Meny(kategorinavn)
        self._kunder = self._lesKundeFil(kundefil)

    def _lesKundeFil(self,kundefil):
        pass

    def _lagOgLeverMat(self,bestilling):
        for rett in bestilling:
            print(rett.rettNavn())    

    def betjenKunde(self,tlf):
        bestilling = self._kunder[tlf].velgRetter(self._meny)
        self._lagOgLeverMat(bestilling)


def hovedprogram():
    takeaway = TakeAway(['Foretter','Hovedretter','Desserter'],'Kunder.txt')

    tlf = input('Venneligst oppgi ditt tlf nr: ')

    while tlf != "\n":
        takeaway.betjenKunde(tlf)
        tlf = input('Venneligst oppgi ditt tlf nr: ')
    
