from abc import ABC


class Vehicle(ABC):

    def __init__(self):
        pass


class Auto:
    def __init__(self, brand, tank_volume, fuel_remaining, speed, mileage):
        self.__brand = brand
        self.__tank_volume = tank_volume
        self.__fuel_remaining = fuel_remaining
        self.__speed = speed
        self.__mileage = mileage
        self.__passengers_number = 0


# passengers_number, airbags_presence


class Motorcycle:
    def __init__(self, brand, tank_volume, fuel_remaining, speed, mileage):
        self.__brand = brand
        self.__tank_volume = tank_volume
        self.__fuel_remaining = fuel_remaining
        self.__speed = speed
        self.__mileage = mileage

# cradle_presence
