class Animal:
    def __init__(self, name):
        self.name = name
class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def say_hello(self):
        return "Мяу!"
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def meet(self, other_cat):
        print(self.name, "почув як кіт каже:", other_cat.say_hello())
cat1 = Cat("Буся", "Британський")
dog1 = Dog("Рекс")
dog1.meet(cat1) 
print(isinstance(cat1, Cat))       
print(issubclass(Cat, Animal))  