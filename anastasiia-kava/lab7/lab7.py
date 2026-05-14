class Phone:
    how_many = 0
    tax = 0.05 

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = float(price) 
        self.price_in_dollars = self.price / 42
        Phone.how_many += 1

    def ring(self):
        return f"{self.brand} {self.model}: Beep! Beep!"

    def info(self):
        return (f"Brand: {self.brand}, Model: {self.model}, "
                f"Price: {self.price:} грн. Долар: {self.price_in_dollars}")

    def apply_tax(self):
        self.price = self.price * (1 + self.tax)
        self.price_in_dollars = self.price / 42

    @classmethod
    def new_tax(cls, new_rate):
        cls.tax = new_rate

    @classmethod
    def get_count(cls):
        return cls.how_many

    @classmethod
    def from_string(cls, phone_str):
        brand, model, price = phone_str.split("-")
        return cls(brand, model, price)

    @staticmethod
    def is_work_hour(hour):
        return 9 <= hour <= 18


Phone.new_tax(0.1) 

phone1 = Phone("Apple", "iPhone 15", 45000)
phone_str = "Google-Pixel 8-32000"
phone2 = Phone.from_string(phone_str)

print(f"Чи працює магазин о 10:00? {Phone.is_work_hour(10)}")


print(f"До податку: {phone1.price} грн")
phone1.apply_tax() 
print(f"Після податку: {phone1.price:} грн")

print(f"Всього телефонів: {Phone.get_count()}")