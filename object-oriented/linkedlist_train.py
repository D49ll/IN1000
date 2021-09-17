class Stasjon:
    def __init__(self, navn):
        self._navn = navn
        self._neste = None

    def sett_neste_stasjon(self, neste):
        self._neste = neste

    def hent_navn(self):
        return self._navn

    def hent_neste_stasjon(self):
        return self._neste

def main():
    
    trikkestall = Stasjon("Trikkestall")
    forrige = trikkestall
    for stasjonsnavn in open("inout/trase.txt"):
        denne = Stasjon(stasjonsnavn.strip())
        
        forrige.sett_neste_stasjon(denne)
        forrige = denne

    maal = input("Hvor vil du reise til? ")
    sted = trikkestall
    while maal != sted.hent_navn():
        sted = sted.hent_neste_stasjon()
        print(sted.hent_navn())

    print("Du er fremme")

main()        