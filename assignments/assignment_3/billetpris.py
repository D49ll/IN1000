'''Oppgave 3: Billettpris

1.  Lag en prosedyre som inneholder variabel alder og be brukeren om å skrive alder på kjøperen
2.  Utvid prosedyren med en variabel billettpris
'''

def billettpris(alder):

    if alder < 18:#Kunden er under eller akkuratt 17år
        pris = 30
        type = "barnebillett"
    elif alder < 63:#Kunden er over 17, men under 63 år
        pris = 50
        type = "voksenbillett"
    else:#Kunden er 63 år eller eldre
        pris = 35
        type = "honorbillett"

    print(f"Prisen for {type} er {pris} kr.")        

kundealder = [15, 31, 63]

for alder in kundealder:
    billettpris(alder) 

'''
Slik jeg ser det så finner jeg ikke noe problem med prosedyren.
'''