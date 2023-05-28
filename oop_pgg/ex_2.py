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

