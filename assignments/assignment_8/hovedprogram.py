from datasenter import Datasenter

def main():
    datasenter = Datasenter()

    filer = ['abel.txt','saga.txt']
    
    for fil in filer:
        datasenter.lesInnRegneklynge(fil)
        print(f'regneklynge for {fil} opprettet.')
    
    datasenter.skrivUtAlleRegneklynger()

main()