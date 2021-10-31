from regneklynge import Regneklynge

def testRegneklynge():
    '''
    En prosedyre som tester Regneklynge klassen.

    Forventet resultat med abel.txt som input er:

    Noder med minst 32 GB: 666
    Noder med minst 64 BG: 666
    Noder med minst 128 GB: 16
    Antall prosessorer: 682
    Antall rack: 56
    '''
    klynge = dict()
    navn = 'abel'

    #Leser fra abel.txt
    f = open('abel.txt').read()
    linjer = f.splitlines()

    #Identifiserer max antall noder pr rack
    noderPerRack = int(linjer[0])
    
    #Oppretter regneklynge
    klynge[navn] = Regneklynge(noderPerRack)

    #Setter inn noder i racks til regneklyngen
    for i in range(1,len(linjer)):
        noder, minne, antPros = linjer[i].split(' ')
        for i in range(int(noder)):
            klynge[navn].settInnNode((int(minne), int(antPros)))


    #Test variabler
    paakrevdMinne = [32,64,128]
    antNoder = []
   
    #Sjekker minne i alle noder mot aktuelt minnekrav
    for minne in paakrevdMinne:
        antNoder.append(klynge[navn].noderMedNokMinne(minne))
    
    #Resultat til terminal
    print()
    print('Resultat:')
    for i in range(len(antNoder)):
        print(f'Noder med minst {paakrevdMinne[i]} GB: {antNoder[i]}')
    print(f'Antall prosessorer: {klynge[navn].antProsessorer()}')
    print(f'Antall rack: {klynge[navn].antRacks()}')
    print()

testRegneklynge()
