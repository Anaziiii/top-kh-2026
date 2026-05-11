class Phone:

    how_many = 0

    dollar = 41

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.dollars = self.price / Phone.dollar
        Phone.how_many += 1

    def info(self):
        return (f"Бренд: {self.brand} Модель: {self.model}"
                f"Ціна: {self.price} грн $: {self.dollars}")

    def new_dollar(self, dollar):

        self.dollars = self.price / dollar


phone1 = Phone("Apple", "iPhone 15", 45000)
phone2 = Phone("Samsung", "S23", 38000)


print(f"Кількість: {Phone.how_many}")

print(phone1.info())
print(phone2.info())

print("Долар 42 для обох")


phone1.new_dollar(42)
phone2.new_dollar(42)


print(phone1.info())
print(phone2.info())