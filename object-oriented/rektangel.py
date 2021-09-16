class Rektangel:

    def __init__(self, lengde, bredde):
        self._lengde = lengde
        self._bredde = bredde

    # Lager en metode som sammenligner to instanser av klassen
    def __eq__(self, annen):
        return(self._lengde == annen._lengde and self._bredde == annen._bredde)    

    def areal(self):
        return self._lengde * self._bredde

    def endre(self, lengde, bredde):
        self._lengde += lengde
        self._bredde += bredde    