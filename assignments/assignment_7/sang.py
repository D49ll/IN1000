class Sang:
    def __init__(self, artist, tittel):
        self._artist = artist
        self._tittel = tittel

    def spill(self):
        print(f"Spiller nå: \'{self._tittel}\' av {self._artist}.")

    def sjekkArtist(self, navn):
        '''
        Inn:
        En streng, navn.

        Ut:
        Basert på om et eller flere av navnene i strengen navn finnes i
        instansvariablen _artist, returneres True eller False
        '''
        navn = navn.lower().split()
        artist = self._artist.lower().split()

        for n in navn:
            for a in artist:
                if n == a:
                    return True
        return False           

    def sjekkTittel(self, tittel):
        '''
        Inn: 
        En streng, tittel.

        Ut:        
        Basert på om oppgitt tittel er den samme som instansvariabelen _tittel, 
        returneres True eller False. 
        '''
        if tittel.lower() == self._tittel.lower():
            return True
        return False

    def sjekkArtistOgTittel(self, artist, tittel):
        '''
        Inn:
        To strenger, artist og tittel.

        Ut:
        True eller False basert på utfallet av sjekkTittel og sjekkArtist.
        '''
        if self.sjekkTittel(tittel) and self.sjekkArtist(artist):
            return True
        return False



