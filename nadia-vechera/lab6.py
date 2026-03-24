class Flower:
    # Змінна класу (спільна для всіх екземплярів)
    total_flowers_count = 0

    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.total = quantity * price
        
        # Збільшуємо лічильник при кожному створенні об'єкта
        Flower.total_flowers_count += 1

    def __str__(self):
        return f"{self.name}: {self.quantity} шт. за {self.total} грн"

    @classmethod
    def get_total_count(cls):
        #Метод класу, що використовує змінну класу
        return f"Загальна кількість створених об'єктів-квітів: {cls.total_flowers_count}"

# Створення об'єктів
f1 = Flower("Троянди", 5, 100)
f2 = Flower("Ромашки", 15, 40)
f3 = Flower("Тюльпани", 10, 50)


print(f1)
print(f2)
print(f3)


# Використання змінної класу через метод
print(Flower.get_total_count())

# Перевірка окремої ціни 
print(f"Окрема ціна першої квітки: {f1.price} грн")