import copy

class Phone:
    tax = 0.05 

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = float(price) 
        self.price_in_dollars = self.price / 42

    def clone(self):
        return copy.deepcopy(self)

    def ring(self):
        return f"{self.brand} {self.model}: Beep! Beep!"

    def info(self):
        return (f"Brand: {self.brand}, Model: {self.model}, "
                f"Price: {self.price} грн. Долар: {self.price_in_dollars:.2f}")

    def apply_tax(self):
        self.price = self.price * (1 + self.tax)
        self.price_in_dollars = self.price / 42


iphone_15 = Phone("Apple", "iPhone 15", 45000)

iphone_15_pro = iphone_15.clone()

iphone_15_pro.model = "iPhone 15 Pro"
iphone_15_pro.price = 55000
iphone_15_pro.price_in_dollars = iphone_15_pro.price / 42

print("Без шаблона:", iphone_15.info())
print("Шаблон:    ", iphone_15_pro.info())