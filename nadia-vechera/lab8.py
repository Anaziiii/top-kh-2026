#Наслідування та використання super()
class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return f"{self.name} видає звук."

class Dog(Animal):
    def __init__(self, name, breed):
        # Використання super() для виклику конструктора батьківського класу
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return f"{self.name} гавкає!"

    def fetch(self):
        return f"{self.name} приносить м'ячик."

class Cat(Animal):
    def speak(self):
        return f"{self.name} м'явкає!"
    
#Використання методів об'єктів іншого дочірнього класу   
class Trainer:
    def train_animal(self, animal_instance):
        # Використання методів об'єкта іншого класу
        print(f"Тренер працює з {animal_instance.name}: {animal_instance.speak()}")




#Методи isinstance та issubclass
# Створюємо екземпляри
my_dog = Dog("Сірко", "Вівчарка")
my_cat = Cat("Мурчик")

# Перевірка isinstance (чи є об'єкт екземпляром класу)
print(isinstance(my_dog, Dog))    # True
print(isinstance(my_dog, Animal)) # True (бо Dog наслідує Animal)
print(isinstance(my_cat, Dog))    # False

# Перевірка issubclass (чи є клас нащадком іншого класу)
print(issubclass(Dog, Animal))    # True
print(issubclass(Animal, Dog))    # False
    




    