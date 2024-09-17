from datetime import datetime

class Auto:

    def __init__(self, manufacturer, brand, fuel_consumption, manufacture_year=2020):
        self.manufacture_year = manufacture_year
        self.manufacturer = manufacturer
        self.brand = brand
        self.fuel_consumption = fuel_consumption
        self.mileage = 0

    def __str__(self):
        return f'<Auto> manufacture year: {self.manufacture_year}, ' \
               f'manufacturer: {self.manufacturer}, ' \
               f'brand: {self.brand}, ' \
               f'fuel consumption: {self.fuel_consumption}'

    @property
    def current_car_age(self):
        its_age = (datetime.today().year - self.manufacture_year)
        return its_age


car1 = Auto(manufacture_year=2019, manufacturer='BMW', brand='M5', fuel_consumption=20.5)
car2 = Auto(manufacture_year=2010, manufacturer='BMW', brand='M5', fuel_consumption=20.5)
car3 = Auto(manufacture_year=2015, manufacturer='BMW', brand='M5', fuel_consumption=20.5)
car4 = Auto(manufacturer='Mercedes', brand='AMG', fuel_consumption=20.5)


print(car1.current_car_age)
print(car2.current_car_age)
print(car3.current_car_age)
print(car4.current_car_age)
