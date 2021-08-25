# 01.15: test matte
'''
Skriv en program som program som ber brukeren om å gjøre enkle beregninger 
(for eksempel: 1 + 1, 5 * 4, 10 / 2).
Hver gang brukeren gir det riktige svaret, blir det neste spørsmålet stilt. 
Hvis brukeren gir et feil svar, skriv ut "du tapte!", 
hvis brukeren svarer på alle spørsmålene riktig, skriv ut "du vant!"
'''

svar = input("Hva er 1 + 1?\n")

if svar == "2":
    print("Riktig!\n")
    svar = input("Hva er 5 * 4?\n")
    if svar == "20":
        print("Riktig!\n")
        svar = input("Hva er 10 / 2?\n")
        if svar == "5":
            print("du vant!")
        else:
            print("du tapte!")
    else:
        print("du tapte!")
else:
    print("du tapte!")