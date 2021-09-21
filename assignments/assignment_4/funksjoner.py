'''
Oppgave 1: Parametere og returverdier
'''
#1.1
def add(num1, num2):
    return num1 + num2

print(f"sum: {add(20,10)}")
print(f"sum: {add(20,20)}")

#1.2 og 1.3
def count_occurrences(my_txt, my_char):
    occur =  0

    #Sjekker hver char i input streng mot brukerinput
    for char in my_txt:
        if char == my_char:
            occur += 1

    return occur

def main():
    my_txt = input("Skriv en tekst: ")
    my_char = input("Skriv en bokstav: ")

    occur = count_occurrences(my_txt,my_char)
    print(f"\"{my_char}\" gjentas {occur} ganger i teksten: \"{my_txt}\"")

main()