class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year


class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model

    def drive():
        print("Driving the car ...")


class Bike(Vehicle):
    def __init__(self, brand, year, type):
        super().__init__(brand, year)
        self.type = type

    def ride():
        print("Riding the bike ...")


car = Car("Toyota", 2020, "Corolla")
bike = Bike("Giant", 2018, "mountain")
Car.drive()
Bike.ride()
