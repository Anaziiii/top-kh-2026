class Car:

    counter_cars = 0
    car_max_speed = 200

    def __init__(self, brand, model, year, probih):
        self.brand = brand
        self.model = model
        self.year = year
        self.probih = probih
        self.speed = 0

        self.your_car = brand + " " + model

        Car.counter_cars += 1
    
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

bmw_m3.speed = 50
tesla.assist_gasoline_car(bmw_m3)

print(f"tesla is ElectricCar? {isinstance(tesla, ElectricCar)}") 

print(f"tesla це Car? {isinstance(tesla, Car)}") 

print(f"GasolineCar Inheritance from Car? {issubclass(GasolineCar, Car)}")

print(f"Car Inheritance from GasolineCar? {issubclass(Car, GasolineCar)}")