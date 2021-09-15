tallene = [12, 11, 11, 16]
innenfor = True

for tall in tallene:
    #Dersom tallet er innenfor intervallet 10 < tall < 20
    #så går sjekken videre til neste tall
    if 10 < tall and tall < 20:
        continue
    
    #Dersom den ikke er innefor intervallet så vil innenfor settes
    #til false. Siden sjekken kun er at en av verdiene ikke er innefor vil 
    #man kunne breake løkken.
    innenfor = False
    break    


print(innenfor)