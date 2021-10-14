from sang import Sang

class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

    def lesFraFil(self, filnavn):
        '''
        Åpner oppgitt fil og leser inn data om sanger.
        Oppretter et sang-objekt for hver linje.
        Legger hvert sang-objekt til en spilleliste
        '''

        for linje in open(filnavn,"r"):
            tittel, artist = linje.strip().split(";")
            self._sanger.append(Sang(artist, tittel))

    def leggTilSang(self, nySang):
        '''
        Legger til en ny sang i spilleliste
        '''

        self._sanger.append(nySang)

    def fjernSang(self, sang):
        '''
        Fjerner en sang fra spillelisten
        '''

        self._sanger.remove(sang)
    
    def spillSang(self, sang):
        '''
        Spiller av ønsket sang
        '''
        sang.spill()

    def spillAlle(self):
        '''
        Spiller av alle sanger i spillelisten til objektet
        '''

        for sang in self._sanger:
            self.spillSang(sang)
        
        '''
        For-løkken er over er ekvivalent med løkken under,
        som er kommentert ut.
        Velger å bruke førstnevnte da dette er mer pythonic kode

        for i in range(len(self._sanger)):
            self.spillSang(self._sanger[i])
        '''
        
    def finnSang(self, tittel):
        '''
        Inn:
        En streng, tittel

        Ut:
        Returnerer et sang-objekt basert på tittel, dersom det finnes i spillelisten
        Dersom det ikke finnes returneres None
        '''

        for sang in self._sanger:
            if sang.sjekkTittel(tittel):
                return sang
        return None

    def hentArtistUtvalg(self, artistnavn):
        '''
        Inn:
        En streng, artistnavn

        Ut:
        En liste, utvalg, som inneholder alle sangene fra spillelisten for
        oppgitt artist. Skulle artisten ikke finnes i spillelisten returneres
        en tom liste.
        '''

        utvalg = []
        for sang in self._sanger:
            if sang.sjekkArtist(artistnavn):
                utvalg.append(sang)
        
        return utvalg