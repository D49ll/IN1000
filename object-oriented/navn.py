class Navn:
    def __init__(self, fornavn, mellom, etter):
        self._fornavn = fornavn
        self._mellom = mellom
        self._etter = etter

    def sortert(self):
        alf_navn = self._etter + ", " + self._fornavn + " " + self._mellom
        return alf_navn

    def naturlig(self):
        nat_navn = self._fornavn + " " + self._mellom + " " + self._etter
        return nat_navn    