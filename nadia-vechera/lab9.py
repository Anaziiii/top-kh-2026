class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        # Базова поведінка (буде перевизначена)
        return f"{self.name} видає невідомий звук."

    def __str__(self):
        # "Магічний метод" для текстового представлення об'єкта
        return f"Тварина: {self.name}"

class Dog(Animal):
    def __init__(self, name, breed):
        # Використання super() для ініціалізації імені через батьківський клас
        super().__init__(name)
        self.breed = breed

    def speak(self):
        # Перевизначення методу (Поліморфізм)
        return f"{self.name} гавкає (Гав-гав!)"

    def fetch(self, item):
        return f"{self.name} приносить {item}."

class Cat(Animal):
    def speak(self):
        # Перевизначення методу (Поліморфізм)
        return f"{self.name} м'явкає (Мяу!)"

    def __len__(self):
        # Ще один "магічний метод" (наприклад, довжина імені)
        return len(self.name)

class Trainer:
    def train(self, animal_instance):
        # Взаємодія з об'єктом іншого класу
        print(f"Початок тренування...")
        print(f"Результат: {animal_instance.speak()}")

# --- Перевірка результатів ---

my_dog = Dog("Сірко", "Вівчарка")
my_cat = Cat("Мурчик")
pro_trainer = Trainer()

# 1. Поліморфізм у дії
pro_trainer.train(my_dog)
pro_trainer.train(my_cat)

# 2. Магічні методи
print(my_dog)          # Спрацював __str__
print(len(my_cat))     # Спрацював __len__

# 3. Перевірка типів
print(f"Чи є Сірко твариною? {isinstance(my_dog, Animal)}")
print(f"Чи є Cat підкласом Animal? {issubclass(Cat, Animal)}")