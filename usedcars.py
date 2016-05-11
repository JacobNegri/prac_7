
from car import Car

def main():
    bus = Car(100)
    bus.drive(40)
    print("fuel =", bus.fuel)
    print("odo =", bus.odometer)
    print(bus)

    limo = Car(1500)
    limo.add_fuel(20)
    print("fuel =", limo.fuel)
    print("odo =", limo.odometer)
    print(limo)

    limo2 = Car(19)
    limo2.drive(115)
    print("odo =", limo2.odometer)
    print(limo2)



main()