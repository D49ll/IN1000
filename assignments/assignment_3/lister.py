'''Oppgave 1: Lister

1.  Lag en liste fylt med 3 tall. 
    Legg deretter til et nytt tall på slutten av listen.
    Skriv ut det første og tredje elementet i lista.
'''

min_liste = [3, 2, 1]
min_liste.append(4) #Legger til 4 på enden av min_liste

print(f"Første element i listen er {min_liste[0]}.\nTredje elememnt i listen er {min_liste[2]}")

'''
2.  Lag en ny, tom liste. 
    Be deretter brukeren om å oppgi 4 navn, 
    legg disse inn i lista.
'''

tom_liste = []

for i in range (4):
    tom_liste.append(input("Oppgi et navn: ").lower())


'''
3.  Bruke en if-sjekk for å se om brukeren har lagt inn navnet ditt i lista.
    Hvis brukeren har gjort det skal du skrive ut "Du husket meg!".
    Hvis navnet ditt ikke finnes i lista skal du skrive ut "Glemte du meg?"
'''

if "daniel" in tom_liste: #dersom "daniel" finnes i listen vil dette være sant
    print("Du husket meg!")
else:
    print("Glemte du meg?")

'''
4.  Beregn summen og produketet av tallene i den første rekka,
    legg disse to tallene i en ny liste. Lag enda en liste ved å slå
    sammen den opprinnelige tall-listen med listen som inneholder sum 
    og produkt. Fjern deretter de to siste elementene fra listen
    og skriv den ut på nytt.
'''
#Definerer et funksjon for å finne produktet av alle elementene i en liste
def prod(list):
    '''
    Regner ut produktet av alle elementene i en liste
    '''
    n = len(list)
    product = 1
    for i in range(0, n):
        product *= list[i]
    
    return product

#Lager en ny liste som inneholder sum og produkt av elementene i min_liste
res_liste = [sum(min_liste),prod(min_liste)]

#Konkatenerer listene
sammensatt_liste = min_liste + res_liste

print(sammensatt_liste)

#Fjerner to siste elementene i listen
del sammensatt_liste[-2:] # -2 er nest siste element i listen.

print(sammensatt_liste)