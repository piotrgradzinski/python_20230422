class Train:
    def __init__(self, speed=10, fuel=1):
        self.speed = speed
        self.fuel = fuel

    def get_info(self) -> str:
        return f'My speed is {self.speed}. I have {self.fuel} litr fuel in my tank.'

    def __str__(self):
        return self.get_info()

    def speed_up(self, new_speed: int):
        if new_speed > self.speed + 0.75 * self.speed:
            raise ValueError('New speed must be less than 75% of current speed.')
        if self.fuel - (new_speed - self.speed) * (self.speed/100) < 0:
            raise ValueError('Incresing speed to this level will drain the fuel.')
        self.fuel = self.fuel - (new_speed - self.speed) * (self.speed/100)
        self.speed = new_speed


my_train = Train()
print(my_train)

my_train.speed_up(14)
print(my_train)

my_train.speed_up(16)
print(my_train)

my_train.speed_up(18)
print(my_train)
