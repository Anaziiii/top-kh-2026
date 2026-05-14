class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    @property
    def brand(self):
        return self._brand.upper()

    @brand.setter
    def brand(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._brand = value
        else:
            self._brand = "Unknown"

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            print("Помилка: Ціна не може бути від'ємною!")
            self._price = 0

    @price.deleter
    def price(self):
        print(f"Дані про ціну {self.model} видалено")
        self._price = 0

    @property
    def dollar_price(self):
        return round(self._price / 42, 2)

class Watch(Phone):
    def __init__(self, brand, model, price, metal):
        super().__init__(brand, model, price)
        self.metal = metal

    @property
    def info(self):
        return f"Годинник {self.brand} {self.model} ({self.metal})"


phone = Phone("apple", "iPhone 15", 35000)
print(f"Бренд: {phone.brand}")
print(f"Ціна: {phone.price} грн (${phone.dollar_price})")

phone.price = 38000
print(f"Нова ціна: {phone.price}")

del phone.price
print(f"Ціна після видалення: {phone.price}")

watch = Watch("Samsung", "Galaxy Watch", 12000, "Titanium")
print(watch.info)
