from datetime import datetime

class Car:
    counter_cars = 0
    car_max_speed = 200

    def __init__(self, brand, model, year, probih):
        self.brand = brand
        self.model = model
        self.year = int(year)
        self.probih = float(probih)
        self.speed = 0
        Car.counter_cars += 1

    @property
    def full_name(self):
        return f"{self.brand} {self.model}"

    @full_name.setter
    def full_name(self, name_str):
        brand, model = name_str.split(' ')
        self.brand = brand
        self.model = model

    @full_name.deleter
    def full_name(self):
        self.brand = None
        self.model = None

    def __repr__(self):
        return f"Car('{self.brand}', '{self.model}', {self.year}, {self.probih})"

    def __str__(self):
        return f"{self.full_name} ({self.year})"

    def __add__(self, other):
        if isinstance(other, Car):
            return self.probih + other.probih
        return NotImplemented

    def __len__(self):
        current_year = datetime.now().year
        return current_year - self.year
    
    def acceleration(self):
        if self.speed < Car.car_max_speed:
            self.speed += 10
            print(f"Speed: {self.speed} km/h")
        else:
            print("your speed is MAX")
    
    def slowingDown(self):
        if self.speed >= 10:
            self.speed -= 10
        else:
            print("you are standing")

    def get_description(self):
        return (f"Car: {self.full_name}\n"
                f"Car year: {self.year}\n"
                f"Probih: {self.probih} км\n"
                f"Current speed: {self.speed} km/h")
    
    @classmethod
    def new_car(cls, car_str):
        brand, model, year, probih = car_str.split(' ')
        return cls(brand, model, year, probih)
    
    @staticmethod
    def km_to_miles(probih_km):
        return round(float(probih_km) / 1.6)

class ElectricCar(Car):
    def __init__(self, brand, model, year, probih, battery_capacity):
        super().__init__(brand, model, year, probih)
        self.battery_capacity = battery_capacity
    
    def get_description(self):
        return f"{super().get_description()}\nBattery: {self.battery_capacity} kWh"

class GasolineCar(Car):
    def __init__(self, brand, model, year, probih, fuel_tank):
        super().__init__(brand, model, year, probih)
        self.fuel_tank = fuel_tank
        
    def get_description(self):
        return f"{super().get_description()}\nFuel Tank: {self.fuel_tank} liters"

tesla = ElectricCar("Tesla", "Model S", 2023, 5000, 100)

print(tesla.full_name)

tesla.full_name = "Tesla Model X" 
print(tesla.full_name)

del tesla.full_name
print(tesla.brand, tesla.model)