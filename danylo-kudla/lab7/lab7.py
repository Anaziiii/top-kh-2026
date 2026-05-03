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

    @classmethod
    def set_inflation(cls, amount):
        cls.inflation = amount

    @classmethod
    def from_string(cls, elm_str):
        name, age, chip, money = elm_str.split("-")
        return cls(name, age, chip, money)

    @staticmethod
    def is_walk_time(hour):
        if 8 <= hour <= 22:
            return True
        return False


Dog.set_inflation(0.8)
odj1 = Dog("Bars", 12, 4434, 105)
odj2 = Dog("Уртай", 4, 9264, 680)

paddock = Dog.is_walk_time(6)
print(paddock)

elm_str_1 = "Man-8-8754-50000"
new_el_1 = Dog.from_string(elm_str_1)


odj1.level_inflation()
odj2.level_inflation()
print(Dog.counter)
print(odj1.get_info())
print(odj2.get_info())
