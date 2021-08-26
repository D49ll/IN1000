# Oppgave 3.3 (frivillig)

# Brukerinput
date1 = input("Oppgi en dato (ddmm): ")
date2 = input("Oppgi enda en dato (ddmm): ")

# 



def is_valid(input_date):
    '''
    A function that verifies correct date format
    '''
    str_len = len(input_date)
    digit_format = 2
    split_date = []

    #Sjekk at lengden på stringen riktig
    if str_len > 4: 
        print("For mange inputs, venneligst prøv igjen!")
        return False

    #Sjekker at alle elementene i stringen er integers
    for i in range(str_len):
        #Dersom et element ikke er en int vil int() kaste en error
        try: 
            int(input_date[i])
        except ValueError:
            print("Feil format, venneligst prøv igjen!")
            return False
    
    #Splitter dato inn i dag og måned
    for i in range(0,str_len,digit_format):
        split_date.append(int(input_date[i:i+digit_format]))

    #Sjekker månedsformatet ikke er feil
    if split_date[1] < 13:
        if split_date[1] == 2:
            if split_date[0] < 29 #Regner ikke med skuddår

        elif split_date[1]%2 == 1 or      
    else:


    
        
  


    