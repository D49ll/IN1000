'''
Oppgave 4: Kodeforståelse

Del 1.
Spørsmål: Vil dette programmet kjøre?

Del 2.
Spørsmål: Hvilke problemer vil vi kunne møte på når vi kjører denne koden?

Svar til både Del 1 og 2:
Nei, dette programmet vil ikke kjøre. Utrykket i print() har en syntax feil. 
b er type int, mens "Hei!" er type str. En slik kombinasjon fungerer ikke.
Hadde vi kjørt denne koden ville vi fått en feilmelding om syntax feil.

Dersom vi hadde erstattet b med a i utrykket vil det vær lovlig kode, da a er type str.
    print(a + "Hei")
Eventuelt kunne vi kastet b til str ved å skrive str(b).
    print(str(b) + "Hei")

Selv om vi hadde fikset koden med dette, vil vi enda kunne møte problemer dersom 
det vi taster inn i input() ikke er heltall. 
Dersom det ikke er et heltall vil ikke b = int(a) være gyldig.
'''

a = input("Tast inn et heltall! ")
b = int(a)
if b < 10:
    print(b + "Hei")