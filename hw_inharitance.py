from abc import ABC, abstractmethod
from enum import Enum


class CONFIG(Enum):
    TANK_VOLUME = 60


class Vehicle(ABC):

    def __init__(self, brand, fuel_remaining, speed, mileage):
        self.brand = brand
        self.tank_volume = CONFIG.TANK_VOLUME.value
        self.fuel_remaining = fuel_remaining
        self.speed = speed
        self.mileage = mileage

    def refueling(self, liters):
        self.fuel_remaining += liters
        if self.fuel_remaining > CONFIG.TANK_VOLUME.value:
            self.fuel_remaining = CONFIG.TANK_VOLUME.value

    @abstractmethod
    def __str__(self):
        return f'{self.brand}, has {self.fuel_remaining} fuel left'


class Auto(Vehicle):
    def __init__(self, brand, fuel_remaining, speed, mileage, passengers_number=4, airbags_presence=True):
        super().__init__(brand, fuel_remaining, speed, mileage)
        self.passengers_number = passengers_number
        self.airbags_presence = True

    def transfusion(self, liters, other: Vehicle):
        if self.fuel_remaining > 0:
            self.fuel_remaining -= liters
            other.fuel_remaining += liters
            if self.fuel_remaining >= CONFIG.TANK_VOLUME.value:
                print('Can not continue, tank is full')
            else:
                print('Still filling the tank')  #?
        else:
            print('Not enough fuel:(')

    def __str__(self):
        # if vizov funkcii refueling otvecaht' eto, else vernut' drugoy zagotovleniy text?
        return f'{self.brand}, has {self.fuel_remaining} fuel left'


class Motorcycle(Vehicle):
    def __init__(self, brand, fuel_remaining, speed, mileage, tank_volume=60, cradle_presence=True):
        super().__init__(brand, fuel_remaining, speed, mileage)
        pass

    def transfusion(self, liters, other: Vehicle):
        if self.fuel_remaining > 0:
            self.fuel_remaining -= liters
            other.fuel_remaining += liters
            if self.fuel_remaining >= CONFIG.TANK_VOLUME.value:
                print('Can not continue, tank is full')
            else:
                print('Still filling the tank')  #?
        else:
            print('Not enough fuel:(')

    def __str__(self):
        return f'{self.brand}, has {self.fuel_remaining} fuel left'


car = Auto(brand='Lamborghini', fuel_remaining=20, speed=260, mileage=10000)
motorbike = Motorcycle(brand='Lamborghini', fuel_remaining=15, speed=240, mileage=1000)
# # print(car)
# car.refueling(500)
# print(car)
# print(motorbike)
# motorbike.refueling(500)
# print(motorbike)
car.transfusion(motorbike)

