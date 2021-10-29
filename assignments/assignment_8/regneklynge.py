from rack import Rack

class Regneklynge:
    def __init__(self, noderPerRack):
        self._noderPerRack = noderPerRack
        self._racks = [Rack(noderPerRack)]
        self._i= 0

    def settInnNode(self,node):
        if self._racks[self._i]._rackFult():
            self._i +=1
            self._racks.append(Rack(self._noderPerRack))

        self._racks[self._i].settInn(node)
        print(f'i={self._i}')
        print(self._racks[self._i].getAntNoder())
        
    def antProsessorer(self):
        pass

    def noderMedNokMinne(self,paakrevdMinne):
        pass

    def antRacks(self):
        pass