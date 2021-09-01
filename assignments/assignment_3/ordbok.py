'''Oppgave 2: Ordbok

1.  Lag en ordbok som skal inneholde varer i en butikk og pris.
    Du skal bruke varenavn som nøkkeverider og varepriser som innholdsverdi.
    Opprett ordboka med følgende varer:
        melk - kr 14.90
        brød - kr 24.90
        yogurt - kr 12.90
        pizza - 39.90
    Skriv ut innholdet i ordboken med en enkel print setning.
'''

def print_varer(varer):
    print("Vi har følgende varer på lager:")
    for  key, value in varer.items(): #item() returner key og value for ordlisten
        print(f"{key} koster {value} kr")
    print()


#Oppretter ordbok
varer = {"melk":14.90, "brod":24.90, "yogurt":12.90, "pizza":39.90}

#Printer innholdet i ordbok
print_varer(varer)

'''
2.  Les inn to varenavn og priser fra brukeren og legg disse til i ordboken
    Skriv ut ordboken på ny.
'''

#Gir bruker mulighet til å legge inn to nye varer
for i in range(2):
    key = input("Legg til en ny vare: ")
    val = float(input("Oppgi pris på varen i kr: "))
    varer.update({key:val})
    print("Vareliste oppdatert\n")


#Printer innholdet i oppdatert ordbok
print_varer(varer)
