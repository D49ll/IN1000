# 01.18 Størst verdi
'''
Skriv et program som tar inn tre forskjellige tall og finner den største verdien.
Hvor mange ganger den gjentas
'''
cpt = 0

a = int(input("Verdi 1: "))
b = int(input("Verdi 2: "))
c = int(input("Verdi 3: "))



if a >= b and a >= c:
    largest = a
    print(f"Det største tallet er {a}")
elif b >= a and b >= c:
    largest = c
    print(f"Det største tallet er {b}")
else:
    largest = c
    print(f"Det største tallet er {c}")


if a == largest:
    cpt += 1
    
if b == largest:
    cpt += 1

if c == largest:
    cpt += 1
    
print(f"Den største verdien er {largest} og den gjentas {cpt} ganger")