'''
Oppgave 3: Reiseplan
'''

#3.1
places = list()

print("Skriv inn 5 reisemål:")

for i in range(5):
    user_in = input(f"Reisemål {i}: ")
    places.append(user_in)

#3.2
clothing = list()
departure = list()

for i in range(5):
    user_in = input(f"Oppgi klær for reisemålet \"{places[i]}\": ")
    clothing.append(user_in)
    user_in = input(f"Oppgi avreisedato for reisemålet \"{places[i]}\": ")
    departure.append(user_in)
    print()

#3.3
travelplanner = list((places,clothing,departure))

#3.4
for i, lists in enumerate(travelplanner):
    print(f"travelplanner[{i}] = {lists}")

#3.5
index1 = int(input("Oppgi en index, fra 0 til 2: "))
index2 = int(input("Oppgi enda en index, fra 0 til 4: "))

if (0 <= index1 and index1 <= 2) and (0 <= index2 and index2 <= 4):
    print(f"Travelplanner[{index1}][{index2}] = {travelplanner[index1][index2]}")
else:
    print("Ugyldig input!")


