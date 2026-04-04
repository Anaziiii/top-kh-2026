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
    
print(Car.counter_cars)

car1 = Car("audi", "a4", 2016, 160000)
car2 = Car("BMW", "M3", 2020, 15600)

print(Car.counter_cars)

for i in range(23):
    car2.acceleration()