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

class HunterDog(Dog):
    def __init__(self, name, age, chip, money, breed):
        super().__init__(name, age, chip, money)
        self.breed = breed

    def action(self):
        return f"Собака {self.name} на полюванні"


class ServiceDog(Dog):
    def __init__(self, name, age, chip, money, hunters=None):
        super().__init__(name, age, chip, money)
        if hunters is None:
            self.hunters = []
        else:
            self.hunters = hunters

    def add_hunter(self, hunter):
        if hunter not in self.hunters:
            self.hunters.append(hunter)

    def remove_hunter(self, hunter):
        if hunter in self.hunters:
            self.hunters.remove(hunter)

    def coordinate_work(self):
        for hunter in self.hunters:
            print(f"{self.name} -> {hunter.action()}")


odj1 = HunterDog("Bars", 8, 4434, 105, "Лайка")
odj2 = HunterDog("Уртай", 4, 9264, 680, "Такса")
odj3 = HunterDog("Дуна", 5, 5436, 489, "Німецька вівчарка")

service_dog_1 = ServiceDog("Локатор", 6, 7536, 1245,[odj1, odj2])
service_dog_2 = ServiceDog("Вій", 8, 7845, 1002, [odj3])
service_dog_1.coordinate_work()
service_dog_2.coordinate_work()

print(isinstance(service_dog_1, Dog))
print(issubclass(HunterDog, Dog))