class Cat:
    def __init__(self, age):
        self.age = age
    def __str__(self):
        return f"Кіт (вік: {self.age})"
    def __eq__(self, other):
        return self.age == other.age
    def __add__(self, other):
        return self.age + other.age
c1 = Cat(3)
c2 = Cat(3)
print("Вивід (__str__):", c1)              
print("Порівняння (__eq__):", c1 == c2)
print("Додавання (__add__):", c1 + c2)     