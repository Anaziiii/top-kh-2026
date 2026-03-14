class Car:
    def __init__(self, brand, model, year, probih):
        self.brand = brand
        self.model = model
        self.year = year
        self.probih = probih
        self.speed = 0
    
    def acceleration(self):
        if self.speed < 200:
            self.speed += 10
        else:
            print("your speed is MAX")
    
    def slowingDown(self):
        if self.speed >= 10:
            self.speed -= 10
        else:
            print("you are standing")

car1 = Car("audi", "a4", 2016, 160000)

car1.acceleration()
print(car1.speed)

car1.slowingDown()
print(car1.speed)

car1.slowingDown()
