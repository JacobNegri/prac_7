
from car import Car

def main():
    bus = Car(180)
    bus.drive(30)
    print("fuel =", bus.fuel)
    print("odo =", bus.odometer)
    print(bus)

    limo = Car(100)
    limo.add_fuel(20)
    print("fuel =", limo.fuel)
    print("odo =", limo.odometer)
    print(limo)

    limo2 = Car(100)
    limo2.drive(115)
    print("odo =", limo2.odometer)
    print(limo2)



main()