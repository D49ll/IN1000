'''
Oppgave 1: Regnefunksjoner
'''

def addisjon(a, b):
    return a+b

def subtraksjon(a, b):
    return a-b

def divisjon(a, b):
    return a/b

def tommer_to_cm(antall_tommer):
    assert antall_tommer > 0
    return antall_tommer * 2.54

def skriv_beregninger():
    num1 = float(input("Skriv inn et tall: "))
    num2 = float(input("Skriv et tall til: "))
    print()
    
    print(f"{num1} + {num2} = {addisjon(num1, num2)}")
    print(f"{num1} - {num2} = {subtraksjon(num1, num2)}")
    print(f"{num1} / {num2} = {divisjon(num1, num2)}")
    print()

    tommer = float(input("Skriv inn lengde i tommer: "))
    print(f"{tommer} tilsvarer {tommer_to_cm(tommer)} cm.")




def main():

    #1.1 og 1.2
    #Addisjonsjekk
    assert addisjon(5,5) == 10
    assert addisjon(-5,-5) == -10
    assert addisjon(5,-5) == 0

    #Subtraksjonsjekk
    assert subtraksjon(4,2) == 2
    assert subtraksjon(-4,-2) == -2
    assert subtraksjon(-4,2) == -6
    
    #Divisjonsjekk
    assert divisjon(4,4) == 1
    assert divisjon(-4,-4) == 1
    assert divisjon(4,-4) == -1

    #1.3
    print(tommer_to_cm(2))

    #1.5
    skriv_beregninger()


main()