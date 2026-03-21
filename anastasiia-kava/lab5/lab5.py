class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.price_in_dollars = self.price / 42

    def ring(self):
        return f"{self.brand} : Beep! Beep!"
    
    def info(self):
        return f"brand: {self.brand} model: {self.model} price: {self.price} price in dollars: {self.price_in_dollars}"

phone1 = Phone("Apple", "iPhone", 6000)
phone2 = Phone("Samsung", "Galaxy", 5000)

print(Phone.ring(phone2))
print(phone2.ring())

print(Phone.info(phone1))
print(phone1.info())
        