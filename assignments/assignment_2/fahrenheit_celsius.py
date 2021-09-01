'''
Oppgave 2: Konvertering

Del 1.
Skriv et program med en variabel som er temperatur i fahrenheit, 
bestem selv hva temperaturen skal være og hva variabelen skal hete.

Del 2.
Skriv ut temperaturen i fahrenheit.

Del 3.
Definer en ny variabel som bruker variabelen i punkt 1 til å finne temperaturen i celsius. 

Del 4.
Skriv ut temperaturen i celsius

Del 5.
Modifiser programmet slik at variabelen for fahrenheitblir gitt via brukerinput.
Sørg for at variablen får en tallverdi.
'''

# Del 1 og 5.
temp_F = float(input("Skriv inn temperaturen i fahrenheit: "))

# Del 2
print(f"Temperaturen er {temp_F} Fahrenheit")

# Del 3
temp_C = (temp_F - 32) * 5/9 #Konverterer fra fahrenheit til celsius

print(f"Temperaturen er {round(temp_C,2)} Celsius")

