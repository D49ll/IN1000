# Oppgave 3.1
'''
Dette programmet tar ikke hensyn til gyldige datoer. 
Dvs bruker kan skrive inn 30 februar uten at programmet vet det er feil.
'''

# Brukerinput
print("\nFørste dato:")
dag1 = input("Dag (heltall): ")
mnd1 = input("Måned (heltall): ")

print("\nAndre dato:")
dag2 = input("Dag (heltall): ")
mnd2 = input("Måned (heltall): ")

# Oppgave 3.2

# Sjekker rekkefølgen på datoene
if mnd1 == mnd2: 
    if dag1 == dag2: 
        print("Samme dato!")
    elif dag1 < dag2: 
        print("Riktig rekkefølge!")
    else:
        print("Feil rekkefølge!")
elif mnd1 < mnd2:
    print("Riktig rekkefølge!")
else: 
    print("Feil rekkefølge!")


