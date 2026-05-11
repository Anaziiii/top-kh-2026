class Animal:
    def __init__(self, name, age=1):
        self.name = name
        self._age = age  # Захищений атрибут (інкапсуляція)

    # 1. Використання декоратора @property (Getter)
    @property
    def age(self):
        """Метод для отримання значення віку"""
        return self._age

    # 2. Реалізація Setter
    @age.setter
    def age(self, value):
        """Метод для встановлення віку з перевіркою коректності"""
        if value > 0:
            self._age = value
        else:
            print("Помилка: Вік має бути додатним числом!")

    # 3. Реалізація Deleter
    @age.deleter
    def age(self):
        """Метод для видалення атрибута віку"""
        print(f"Дані про вік {self.name} видалено.")
        del self._age

    def speak(self):
        return f"{self.name} видає звук."

class Dog(Animal):
    def __init__(self, name, breed, age=1):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        return f"{self.name} гавкає!"

# --- Демонстрація нових функцій ---
my_dog = Dog("Сірко", "Вівчарка", 3)

# Використання getter
print(f"Вік собаки: {my_dog.age}") 

# Використання setter (успішно)
my_dog.age = 5
print(f"Новий вік: {my_dog.age}")

# Спроба встановити некоректний вік
my_dog.age = -10 

# Використання deleter
del my_dog.age