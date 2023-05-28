"""
UML class diagram: https://yuml.me/95131f36.png

Implement an ElectricCar class that replicates the behavior of an electric car.
The class should allow to cover a certain distance, which cannot exceed the maximum range
defined for the car. The car should also have the ability to recharge the battery.

> car = ElectricCar(100)
> car.drive(70)
70
> car.drive(50)
30
> car.drive(50)
0
> car.charge()
> car.drive(50)
50
"""


class ElectricCar:
    def __init__(self, max_range: int):
        self.max_range = max_range
        self.battery_level = self.max_range

    def charge(self):
        self.battery_level = self.max_range

    def drive(self, distance_to_drive: int) -> int:
        if distance_to_drive <= self.battery_level:
            self.battery_level -= distance_to_drive
            return distance_to_drive
        else:
            tmp = self.battery_level
            self.battery_level = 0
            return tmp


car = ElectricCar(100)
print(car.drive(70))  # 70
print(car.drive(50))  # 30
print(car.drive(50))  # 0
car.charge()
print(car.drive(50))  # 50
