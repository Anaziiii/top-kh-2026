class Flower:
    def __init__(self, name, quantity, price):
        
        self.name = name
        self.quantity = quantity
        self.price = price
        

        self.total = quantity * price

    def __str__(self):
        return f"{self.name}: {self.quantity} шт. за {self.total} грн"

f1 = Flower("Троянди", 5, 100)
f2 = Flower("Ромашки", 15, 40)

print(f1)
print(f2)

print(f"Окрема ціна першої квітки: {f1.price}")

        