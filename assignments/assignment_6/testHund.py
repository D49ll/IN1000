from hund import Hund

def main():
    fant = Hund(14,25)

    for _ in range(2):
        fant.run()
        fant.eat(2)
        print(fant.get_weight())

    
    
main()