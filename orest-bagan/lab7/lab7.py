
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

car1 = Car("audi", "a4", 2016, 160000)
car2 = Car("BMW", "M3", 2020, 15600)

car3 =  Car.new_car("Mercedes c-class 2010 230000")
print(car3.brand)

print(Car.km_to_miles(car3.probih))


