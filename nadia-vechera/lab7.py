class Flower:
    # Змінна класу (спільна для всіх екземплярів)
    total_flowers_count = 0

    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.total = quantity * price
        
        # Збільшуємо лічильник при створенні об'єкта
        Flower.total_flowers_count += 1

    def __str__(self):
        return f"{self.name}: {self.quantity} шт. за {self.total} грн"

    # Метод класу для роботи зі змінними класу
    @classmethod
    def get_total_count(cls):
        return f"Загальна кількість створених об'єктів-квітів: {cls.total_flowers_count}"

    #  Альтернативний конструктор (створення з рядка "Назва-Кількість-Ціна")
    @classmethod
    def from_string(cls, flower_str):
        name, quantity, price = flower_str.split("-")
        # Повертаємо новий екземпляр класу
        return cls(name, int(quantity), float(price))

    # 5. Статичний метод (не залежить від стану класу чи об'єкта)
    @staticmethod
    def is_price_valid(price):
        return price > 0

# --- ПЕРЕВІРКА РОБОТИ ---

# Створення об'єктів стандартним способом
f1 = Flower("Троянди", 5, 100)
f2 = Flower("Ромашки", 15, 40)

# Використання альтернативного конструктора
f3 = Flower.from_string("Тюльпани-10-50")

print(f1)
print(f2)
print(f3)

# Використання методу класу для отримання лічильника 
print(f"\n{Flower.get_total_count()}")

# Перевірка роботи статичного методу 
test_price = -10
if Flower.is_price_valid(test_price):
    print(f"Ціна {test_price} є коректною.")
else:
    print(f"Ціна {test_price} некоректна (має бути більше 0).")