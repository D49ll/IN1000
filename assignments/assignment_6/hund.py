class Hund:
    def __init__(self, alder, vekt):
        self._alder = alder
        self._vekt = vekt
        self._metthet = 10

    def get_age(self):
        return self._alder

    def get_weight(self):
        return self._vekt

    def run(self):
        self._metthet -= 1

        if self._metthet < 5:
            self._vekt -= 1

    def eat(self, metthet):
        self._metthet += metthet    
        
        if self._metthet > 7:
            self._vekt += 1