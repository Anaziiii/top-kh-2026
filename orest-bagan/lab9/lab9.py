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

        self.your_car = brand + " " + model

        Car.counter_cars += 1

    def __repr__(self):
        return f"Car('{self.brand}', '{self.model}', {self.year}, {self.probih})"

    def __str__(self):
        return f"{self.your_car} ({self.year})"

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
            print(self.speed)
        else:
            print("your speed is MAX")
    
    def slowingDown(self):
        if self.speed >= 10:
            self.speed -= 10
        else:
            print("you are standing")

    def get_description(self):
        return(f"Car: {self.your_car}\n"
                f"Car year: {self.year}\n"
                f"Probih: {self.probih} км\n"
                f"Current speed: {self.speed} km/h")
    
    @classmethod
    def new_car(cls, car_str):
        brand, model, year, probih = car_str.split(' ')
        return cls(brand, model, year, probih)
    
    @classmethod
    def change_max_speed(cls, new_speed):
        cls.car_max_speed = new_speed
    
    @staticmethod
    def km_to_miles(probih_km):
        probih_miles = round(float(probih_km) / 1.6)
        return probih_miles
    

class ElectricCar(Car):
    def __init__(self, brand, model, year, probih, battery_capacity):
        super().__init__(brand, model, year, probih)
        self.battery_capacity = battery_capacity
    
    def get_description(self):
        parent_desc = super().get_description()
        return f"{parent_desc}\nBattery: {self.battery_capacity} kWh"

    def assist_gasoline_car(self, gas_car):
        print(f"Electric car {self.brand} help Gasoline car {gas_car.brand}")
        gas_car.slowingDown()
        

class GasolineCar(Car):
    def __init__(self, brand, model, year, probih, fuel_tank):
        super().__init__(brand, model, year, probih)
        self.fuel_tank = fuel_tank
        
    def get_description(self):
            parent_desc = super().get_description()
            return f"{parent_desc}\nFuel Tank: {self.fuel_tank} liters"
    
tesla = ElectricCar("Tesla", "Model S", 2023, 5000, 100)
bmw_m3 = GasolineCar("BMW", "M3", 2021, 12000, 60)

print(tesla)

print(repr(bmw_m3))

total_probih = tesla + bmw_m3
print(total_probih)

print(len(bmw_m3))