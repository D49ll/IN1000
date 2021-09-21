from sang import Sang

class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

    def lesFraFil(self, filnavn):
        for linje in open(filnavn,"r"):
            tittel, artist = linje.strip().split(";")
            self._sanger.append(Sang(artist, tittel))

    def leggTilSang(self, nySang):
        self._sanger.append(nySang)

    def fjernSang(self, sang):
        
        self._sanger
