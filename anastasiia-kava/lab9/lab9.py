class Phone:
    how_many = 0

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model

        self.price = price 
        Phone.how_many += 1


    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            print(f"Помилка: Ціна для {self.model} не може бути від'ємною!")
            self._price = 0
        else:
            self._price = value

    @price.deleter
    def price(self):
        print(f"Інформацію про ціну {self.model} видалено.")
        del self._price


    @property
    def price_in_dollars(self):

        return round(self._price / 42, 2)

    def __repr__(self):
        return f"Phone('{self.brand}', '{self.model}', {self.price})"

    def __str__(self):
        return f"{self.brand} {self.model} {self.price} грн ({self.price_in_dollars})"

    def __gt__(self, other):
        if isinstance(other, Phone):
            return self.price > other.price
        return NotImplemented

    def __add__(self, other):

        if isinstance(other, Phone):
            combined_model = self.model[:3] + " " + other.model[-3:]
            new_price = self.price + other.price
            return Phone(self.brand, f"Bundle-{combined_model}", new_price)
        return NotImplemented



phone1 = Phone("Apple", "iPhone 15", 35000)
phone2 = Phone("Samsung", "Galaxy S24", 40000)


print(f"Репрезентація: {repr(phone1)}")
print(f"Рядок для користувача: {str(phone1)}")

if phone2 > phone1:
    print(f"{phone2.model} дорожчий за {phone1.model}")


bundle = phone1 + phone2
print(f"Створено комплект: {bundle.model} із загальною ціною {bundle.price} грн")


print(f"Ціна в доларах: ${phone1.price_in_dollars}")
phone1.price = -500 
print(f"Ціна після спроби помилки: {phone1.price} грн")

del phone1.price