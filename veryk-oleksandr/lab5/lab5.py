class House: 
    def __init__(self, address, price, area): 
        self.address = address 
        self.price = price 
        self.area = area 

    def get_price_per_square_meter(self): 
        return self.price / self.area 

    def get_full_info(self): 
        return f"Адреса: {self.address}, Ціна: {self.price}, Площа: {self.area} м\u00B2, Ціна за 1м\u00B2: {self.get_price_per_square_meter():.2f}"   
        


address1 = House("Львів, Стрийська, 10", 48000, 32)  
print(address1.get_full_info()) 
print(f"Ціна за квадратний метр: {address1.get_price_per_square_meter():.2f} грн/м\u00B2")

address2 = House("Львів, Сихівська, 15", 60000, 40)
print(address2.get_full_info()) 
print(f"Ціна за квадратний метр: {address2.get_price_per_square_meter():.2f} грн/м\u00B2")  



