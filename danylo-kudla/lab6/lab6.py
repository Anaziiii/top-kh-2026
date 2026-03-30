class Dog:
    counter = 0
    inflation = 0.9

    def __init__(self, name, age, chip, money):
        self.name = name
        self.age = age
        self.chip = chip
        self.money = money
        Dog.counter += 1

    def get_info(self):
        return f"Ім'я: {self.name} Вік: {self.age} Чіп: {self.chip} Монет: {self.money}"

    def level_inflation(self):
        self.money = int(self.money * self.inflation)

odj1 = Dog("Bars", 12, 4434, 105)
odj2 = Dog("Уртай", 4, 9264, 680)
odj1.level_inflation()
odj2.level_inflation()
print(Dog.counter)
print(odj1.get_info())
print(odj2.get_info())
