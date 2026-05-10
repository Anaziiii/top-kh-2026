class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed


    def __repr__(self):
        return "Dog('{}', {}, '{}')".format(self.name, self.age, self.breed)

    def __str__(self):
        return f"{self.name} - {self.age} - {self.breed}"

    def __gt__(self, other):
        if isinstance(other, Dog):
            return self.age > other.age
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Dog):
            combined_name = self.name[:3] + other.name[-3:]
            return Dog(combined_name, 0, self.breed)
        return NotImplemented

dog1 = Dog("Bars", 5, "Вівчарка")
dog2 = Dog("Дуна", 4, "Вівчарка")
print(repr(dog1))
print(str(dog1))

if dog1 > dog2:
    print(f"{dog1.name} старший за {dog2.name}")

puppy = dog1 + dog2
print(f"Цуценя: {puppy.name}")