class Cat():
    animal_type = "Кіт домашній"
    count_cats = 0
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        self.price = 0 
        
        self.breed_dict = {
            "британський": 2000,
            "сфінкс": 3500,
            "сіамський": 2500,
            "мей-кун": 5000,
            "безпородний": 0
        }
        self.set_price()
        Cat.count_cats += 1

    def information(self):
        return {
            "Ім'я": self.name,
            "Порода": self.breed,
            "Вік": self.age,
            "Ціна": self.price
        }

    def set_price(self):
        if self.breed.lower() in self.breed_dict:
            self.price = self.breed_dict[self.breed.lower()]
        else:
            self.price = 500
    def show_animal_type(self):
        return "Ця тварина належить до виду: %s" % Cat.animal_type


animal1 = Cat("Буся", "британський", 3)
animal2 = Cat("Мурзік", "безпородний", 5)

print(animal1.information())
print(animal1.show_animal_type())
print("Всього створено котів:", Cat.count_cats)