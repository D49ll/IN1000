from rack import Rack

class Regneklynge:
    def __init__(self, noderPerRack):
        '''
        Oppretter et Rack object med Node begrensninger som legges i en liste.
        '''
        self._noderPerRack = noderPerRack
        self._racks = [Rack(noderPerRack)]
        self._i = 0

    def settInnNode(self,node):
        '''
        Plasserer en node inn i et rack med ledig plass.
        Oppretter en ny rack dersom nåværende rack er fult
            @param node referanse til noden som skal settes inn i datastrukturen
        '''
        #Oppretter et nytt rack dersom nåværende er fult
        if self._racks[self._i]._rackFult():
            self._i +=1
            self._racks.append(Rack(self._noderPerRack))

        #Legger til node i rack. Mer node variabelen er en tuple
        self._racks[self._i].settInn(node)


    def antProsessorer(self):
        '''
        Beregner totalt antall prosessorer i hele regneklyngen
            @return totalt antall prosessorer
        '''
        totalAntProsessorer = 0
        for rack in self._racks:
            totalAntProsessorer += rack.antProsessorer()

        return totalAntProsessorer


    def noderMedNokMinne(self,paakrevdMinne):
        '''
        Beregner antall noder i regnekungen med minne over angitt grense
            @param paakrevdMinne hvor mye minne skal noder som telles med ha
            @return antall noder med tilstrekkelig inne
        '''
        antNoder = 0
        for rack in self._racks:
            antNoder += rack.noderMedNokMinne(paakrevdMinne)
        
        return antNoder


    def antRacks(self):
        '''
        Henter antall racks i regneklyngen
            @return antall racks
        '''
        return len(self._racks)