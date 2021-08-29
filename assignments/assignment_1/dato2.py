# Oppgave 3.3 (frivillig)
'''
Var usikker på hvordan man kunne gjøre sammenligningen enklere enn i oppgave 3.2.
Jeg prøvde derimot å lage et program som tok hensyn til riktig format av dato og at antall dager stemmer med måned. 
Eks: februar har kun 28 dager, derfor vil 30 dager i februar ikke vær gyldig (tar ikke hensyn til skuddår).
'''
def input_format_valid(input_date):
    '''
    Verifiserer riktig format (ddmm). 
    Verifiserer at elementer i stringen er kun heltall.
    '''
    #Sjekker format
    if len(input_date) > 4: 
        return False

    #Sjekker heltallselementer
    for i in range(len(input_date)):
        try: 
            int(input_date[i])
        except ValueError:
            return False
    
    return True

def str_to_int(input_date):
    '''
    Konverterer en string som inneholder tall til en liste med integers.
    Funksjonen sjekker ikke at stringen kun inneholder heltall. Dersom
    man sender inn en string uten bare heltall vil man få en error.

    Dette er imidlertig ivaretatt av "input_format_valid()" funksjonen
    '''
    #Variabler
    split_date = [] #Tom liste til heltall
    digit_format = 2 #Antall heltall i hvert element av listen

    for i in range(0,len(input_date),digit_format):
            split_date.append(int(input_date[i:i+digit_format]))
    return split_date


def input_date_valid(input_date):
    '''
    Sjekker at dato er gyldig.
    '''

    if input_format_valid(input_date): #Sjekker først at string er gyldig format
        split_date = str_to_int(input_date) #Konverterer deretter string til en liste med heltall

        #Riktig antall måneder
        if split_date[1] < 13:

            #Feb
            if split_date[1] == 2:
                # 29 dager
                if split_date[0] < 29:
                    return True
                else:
                    return False

            #Jan, Mar, Mai, Jul, Aug, Okt, Des
            elif (split_date[1]%2 == 1 and split_date[1] < 8) or (split_date[1]%2 == 0 and split_date[1] > 7):
                # 31 dager
                if split_date[0] < 32:
                    return True
                else:
                    return False

            #Apr, Jun, Sep, Nov
            else:
                # 30 dager
                if split_date[0]<31:
                    return True
                else:
                    return False

        #Feil antall måneder
        else:
            return False

    #Feil stringformat
    else:
        return False

def date_order(input_date1, input_date2):
    '''
    Sjekker rekkefølgen til dato1 og dato2
    '''
    date1 = str_to_int(input_date1)
    date2 = str_to_int(input_date2)

    #Sjekker først om måneder er like
    if date1[1] == date2[1]:
        #Sjekker om dager er like
        if date1[0] == date2[0]: 
            print("\nSamme dato!")
        #Sjekker om dag1 kommer før dag2
        elif date1[0] < date2[0]: 
            print("\nRiktig rekkefølge!")
        #Alle andre tilfeller
        else:
            print("\nFeil rekkefølge!")
    # Dersom måned i date1 kommer før måned i date2        
    elif date1[1] < date2[1]:
        print("\nRiktig rekkefølge!")
    # Alle andre tilfeller    
    else: 
        print("\nFeil rekkefølge!")


# Første dato input
print("Første dato:")
date1 = input("ddmm: ")

while not input_date_valid(date1): #Looper ved ugyldig dato
    print("here")
    date1 = input("Feil format eller ugyldig dato. Venneligst prøv igjen.\nHusk riktig formatering (ddmm)")

# Andre dato input
print("Andre dato:")
date2 = input("ddmm: ")


while not input_date_valid(date2): #Looper ved ugyldig dato
    date2 = input("Feil format eller ugyldig dato. Venneligst prøv igjen.\nHusk riktig formatering (ddmm)")

# Datoer er gyldig og rekkefølgen sjekkes
date_order(date1, date2)
