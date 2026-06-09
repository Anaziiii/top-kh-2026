class House:
    def __init__(self, address, price):
        self._address = address
        self._price = price

    
    @property
    def price(self):
        return self._price


    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            print("Ціна не може бути від’ємною")

    
    @price.deleter
    def price(self):
        print("Ціна видалена")
        self._price = None

    
    @property
    def address(self):
        return self._address



h = House("Львів, Стрийська", 50000)

print(h.price)
h.price = 60000
print(h.price)

del h.price