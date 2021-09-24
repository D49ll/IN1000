from motorsykkel import Motorsykkel

def main():
    bike1 = Motorsykkel(123,'fiat',200)
    bike2 = Motorsykkel(456,'bmw',600)
    bike3 = Motorsykkel(789,'ford',1200)

    bike1.print_info()
    bike2.print_info()
    bike3.print_info()

    bike3.drive(20)
    print(bike3.get_km())

main()
