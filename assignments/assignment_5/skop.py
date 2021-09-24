def minFunksjon():
    for x in range(2):  #Kjøres 2 ganger
        c = 2           #c tilegnes verdien 2
        print(c)        #c printes til terminalen
        c += 1          #c økes med 1
        b = 10          #b tilegnes verdien 10
        b += a          #Feil, a er ikke definert, dette vil terminere programmet
        print(b)
    return(b)

def hovedprogram():
    a = 42              #a tilegnes 42
    b = 0               #b tilegnes 0
    print(b)            #b printes til terminalen
    b = a               #b tilegnes a, som er 42
    a = minFunksjon()   #a settes lik min funksjon, som ikke har noen returnverdi. 
                        #Programmet termineres da minFunksjon() har en ugyldig kodelinje
    print(b)            
    print(a)

hovedprogram()