class Collar:
    def __init__(self, owner_name, phone_number):
        self.owner_name = owner_name
        self.phone_number = phone_number

class Dog:
    def __init__(self, name, age, owner_name, phone_number):
        self.name = name
        self.age = age
        self._chip = Collar(owner_name, phone_number)

    @property
    def chip(self):
        print(f"--- Зчитування даних з чіпа {self.name} ---")
        return f"Власник: {self._chip.owner_name}, Контакт: {self._chip.phone_number}"

    @chip.setter
    def chip(self, data):
        owner, phone = data
        if len(owner) < 2:
            print("Помилка: Ім'я власника коротке!")
        elif not str(phone).isdigit():
            print("Помилка: Номер телефону має містити лише цифри!")
        else:
            print(f"Перезапис даних на чіп для {self.name}...")
            self._chip.owner_name = owner
            self._chip.phone_number = phone

    @chip.deleter
    def chip(self):
        print(f"Дані на чіпі {self.name} анульовано!")
        self._chip.owner_name = "Невідомо"
        self._chip.phone_number = "000"

my_dog = Dog("Уртай", 5, "Василь", "0674315479")
print(my_dog.chip) # --- Зчитування даних з чіпа Уртай ---
                   # Власник: Василь, Контакт: 0674315479

my_dog.chip = ("Олександр", "0501112233") # Перезапис даних на чіп для Уртай...
print(my_dog.chip)                        # Власник: Олександр, Контакт: 0501112233

del my_dog.chip     # Дані на чіпі Уртай анульовано!
print(my_dog.chip)  # Власник: Невідомо, Контакт: 000

