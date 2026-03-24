class Phone:
    how_many = 0
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.price_in_dollars = self.price / 42
        Phone.how_many += 1

    def ring(self):
        return f"{self.brand} : Beep! Beep!"
    
    def info(self):
        return f"brand: {self.brand} model: {self.model} price: {self.price} price in dollars: {self.price_in_dollars}"
    
    @classmethod
    def count(Phone):
        return Phone.how_many

phone1 = Phone("Apple", "iPhone", 6000)
phone2 = Phone("Samsung", "Galaxy", 5000)

print(Phone.count())

print(Phone.ring(phone2))
print(phone2.ring())

print(Phone.info(phone1))
print(phone1.info())


