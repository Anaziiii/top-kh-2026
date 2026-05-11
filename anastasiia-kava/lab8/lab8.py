class Phone:
    how_many = 0

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.price_in_dollars = self.price / 42
        Phone.how_many += 1

    def ring(self):
        return f"{self.brand}: Beep! Beep!"
    
    def info(self):
        return f"brand: {self.brand}, model: {self.model}, price: {self.price}, dollar : {self.price_in_dollars}"
    
    @classmethod
    def count(Phone): 
        return Phone.how_many

class CPU(Phone):

    def __init__(self, brand, model, price, cpu):
        super().__init__(brand, model, price) 
        self.cpu = cpu

    def ring(self):
        cpu_ring = super().ring()
        return f"{cpu_ring} : Wiy! Wiy!"

    def info(self):
        cpu_info = super().info()
        return f"{cpu_info}, CPU: {self.cpu}"

class Watch(Phone):
    def __init__(self, brand, model, price, metal):
        super().__init__(brand, model, price)
        self.metal = metal
    
    def mmetal(self):
        return f"{self.metal}"

class Techno(Watch):
    def test(self, other):
        return f"{other.info()}"

        
watch = Watch("Samsung", "Galaxy Watch", 12000, "Titanium") 
cp1 = CPU("Apple", "MacBook PRO", 80000, "M4 PRO") 
phone1 = Phone("Apple", "iPhone 15", 35000) 
phone2 = Phone("Samsung", "Galaxy S24", 40000) 
techno1 = Techno("Apple", "Diagnostic Pro", 5000, "Titanium")

print(Phone.count())


print(phone1.ring())
print(Phone.info(phone1))

print(phone2.info())
print(Phone.ring(phone2))

print(cp1.info())
print(CPU.info(cp1))
print(CPU.ring(cp1))

print(Watch.mmetal(watch))

print(techno1.test(watch))


isinstance(watch, Watch)
isinstance(watch, Phone)
isinstance(cp1, Watch)

issubclass(Watch, Phone) 
issubclass(Phone, CPU)
