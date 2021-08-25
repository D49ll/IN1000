# Oppgave 3.1
print("\nFørste dato.")
dag1 = input("Dag (heltall): ")
mnd1 = input("Måned (heltall): ")

print("\nAndre dato")
dag2 = input("Skriv dag for andre dato: ")
mnd2 = input("Skriv måned for andre dato: ")

# Oppgave 3.2
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

print("test")