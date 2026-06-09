class House:
    def __init__(self, address, price, area):
        self.address = address
        self.price = price
        self.area = area

    
    def __str__(self):
        return f"House: {self.address}"

    def __len__(self):
        return int(self.area)

    def __add__(self, other):
        return self.price + other.price


class Apartment(House):
    def __str__(self):
        return f"Apartment: {self.address}"


class Villa(House):
    def __str__(self):
        return f"Villa: {self.address}"



h1 = House("Львів", 50000, 40)
h2 = Apartment("Київ", 70000, 60)
h3 = Villa("Одеса", 90000, 80)

print(h1)
print(h2)
print(h3)

print("Площа (len):", len(h1))
print("Сума цін:", h1 + h2)