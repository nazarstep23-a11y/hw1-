class TransportVehicle:
    def __init__(self, speed):
        self.speed = speed

    def move(self):
        print("Moving at speed", self.speed, "km/h")


class Car(TransportVehicle):
    def move(self):
        print("Car is driving at", self.speed, "km/h")


class Motorcycle(TransportVehicle):
    def move(self):
        print("Motorcycle is riding at", self.speed, "km/h")


class Plane(TransportVehicle):
    def move(self):
        print("Plane is flying at", self.speed, "km/h")


car = Car(120)
motorcycle = Motorcycle(90)
plane = Plane(800)

car.move()
motorcycle.move()
plane.move()