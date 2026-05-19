class Cat():
    count_cats = 0
    
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        Cat.count_cats += 1

    def information(self):
        return {"Ім'я": self.name, "Порода": self.breed, "Вік": self.age}

    @classmethod
    def show_count(cls):
        return "Всього створено котів: %d" % cls.count_cats

    @classmethod
    def from_string(cls, info):
        name, breed, age = info.split("-")
        return cls(name, breed, age)

    @staticmethod
    def say_hello():
        return "Мяу-мяу! Я просто кіт."


cat1 = Cat("Буся", "британський", 3)
print(cat1.information())

cat2 = Cat.from_string("Мурзік-безпородний-5")
print(cat2.information())

print(Cat.show_count())

print(Cat.say_hello())