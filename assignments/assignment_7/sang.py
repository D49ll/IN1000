class Sang:
    def __init__(self, artist, tittel):
        self._artist = artist
        self._tittel = tittel

    def spill(self):
        print(f"Spiller {self._tittel} av {self._artist}.")

    def sjekkArtist(self, navn):
        navn = navn.lower().split()
        artist = self._artist.lower().split()

        for sjekk_navn in navn:
            for artist_navn in artist:
                if sjekk_navn == artist_navn:
                    return True
        return False           

    def sjekkTittel(self, tittel):
        if tittel.lower() == self._tittel.lower():
            return True
        return False

    def sjekkArtistOgTittel(self, artist, tittel):
        if self.sjekkTittel(tittel) and self.sjekkArtist(artist):
            return True
        return False



