# 01.17 Matpreferanser
'''
Skriv et program som spør brukeren om deres matpreferanser for å finne et godt måltid for dem. 
Bruk minst to matpreferanser,
for eksempel kjøttspiser/vegetarianer/veganer og glutenallergi/ingen allergi.

Du kan bruke følgende måltider som eksempelmåltider. 
Noen måltider kan brukes i flere scenarier, og hvert måltid bør brukes minst en gang.

    Falafal (vegetarisk og vegansk, glutenfri)
    Lasagne (inneholder kjøtt, gluten)
    Biff (inneholder kjøtt, glutenfri)
    Pizza margherita (vegetarisk, men ikke vegansk, inneholder gluten)

Brukeren kan svare 'ja' eller 'nei'. Hvis du får et annet svar, skriv ut en advarsel.
'''

choose_pref = True
choose_allergi = True

pref = input("Hva er din matpreferanse?\n1 = kjøttspiser, 2 = vegetarianer, 3 = veganer.\n")

#Valg av matpreferanse
while choose_pref:
    if pref == "1":
        pref = "kjøttspiser"
        choose_pref = False
    elif pref == "2":
        pref = "vegetarianer"
        choose_pref = False
    elif pref == "3":
        pref = "veganer"
        choose_pref = False
    else:
        print("Feil input! Velg på ny.")
        pref = input("Hva er din matpreferanse?\n1 = kjøttspiser, 2 = vegetarianer, 3 = veganer\n")

print(f"Du er en {pref}")    

#Valg av gluten allergi
allergi = input("Har du gluten allergi? [y/n]\n")
while choose_allergi:
    if allergi == "n":
        allergi = "nei"
        choose_allergi = False
    elif allergi == "y":
        allergi = "ja"
        choose_allergi = False
    else:
        print("Feil input! Velg på ny.")
        allergi = input("Har du gluten allergi? [y/n]\n")

# Kommuniserer gluten valg
if allergi == "nei":
    print("Du har ikke gluten allergi\n")
else:
    print("Du har gluten allergi\n")

# Alternativer for kjøttspiser
if pref == "kjøttspiser" and allergi == "nei":
    print("Du kan spise: Lasange, Biff")

if pref == "kjøttspiser" and allergi == "ja":
    print("Du kan spise biff")

# Alternativer for vegetarianer
if pref == "vegetarianer" and allergi == "nei":
    print("Du kan spise: Pizza margherita og Falaffel")

if pref == "vegetarianer" and allergi == "ja":
    print("Du kan spise: Falaffel")

# Alternativer for veganer
if pref == "veganer" and allergi == "nei":
    print("Du kan spise Falaffel")

if pref == "veganer" and allergi == "ja":
    print("Du kan spise Falaffel")