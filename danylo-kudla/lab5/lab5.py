class Dog:
    def __init__(self, name, age, chip):
        self.name = name
        self.age = age
        self.chip = chip

    def get_info(self):
        return f"Ім'я: {self.name} Вік: {self.age} Чіп: {self.chip}"

odj1 = Dog("Bars", 12, 4434)
odj2 = Dog("Уртай", 4, 9264)
print(odj1.get_info())
print(odj2.get_info())