class PhoneSpecs:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

class FinancialSystem:
    def apply_tax(self, price):
        return price * 1.05  

class AudioSystem:
    def play_sound(self):
        return "Beep! Beep!"
    
class Customer:
    def __init__(self, name):
        self.name = name

    def update(self, phone_info):
        print(f"[Повідомлення для {self.name}]: {phone_info}")

class PhoneFacade:
    def __init__(self, brand, model, price):
        self.specs = PhoneSpecs(brand, model, price)
        self.finance = FinancialSystem()
        self.audio = AudioSystem()
        self.subscribers = []

    def attach(self, observer):
        self.subscribers.append(observer)

    def detach(self, observer):
        self.subscribers.remove(observer)

    def notify(self):
        info = f"{self.specs.brand} {self.specs.model} змінив ціну! Нова ціна: {self.specs.price:.2f} грн."
        for observer in self.subscribers:
            observer.update(info)

    def apply_tax(self):
        self.specs.price = self.finance.apply_tax(self.specs.price)
        self.notify() 

    def set_discount(self, discount_amount):
        self.specs.price -= discount_amount
        self.notify() 

if __name__ == "__main__":
    iphone = PhoneFacade("Apple", "iPhone 15", 45000)
    customer_1 = Customer("Іван")
    customer_2 = Customer("Марія")

    iphone.attach(customer_1)
    iphone.attach(customer_2)
    
    print("Податок")
    iphone.apply_tax()
    
    print("Марія відписується від сповіщень")
    iphone.detach(customer_2)
    
    print("Знижка")
    iphone.set_discount(2000)