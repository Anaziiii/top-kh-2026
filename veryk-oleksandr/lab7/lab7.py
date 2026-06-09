class House:
    currency = "UAH"
    total_houses = 0

    def __init__(self, address, price, area):
        self.address = address
        self.price = price
        self.area = area
        House.total_houses += 1

    def get_price_per_square_meter(self):
        return self.price / self.area

    
    @classmethod
    def get_currency(cls):
        return cls.currency

    @classmethod
    def set_currency(cls, value):
        cls.currency = value

  
    @classmethod
    def from_string(cls, data):
        address, price, area = data.split(";")
        return cls(address, float(price), float(area))

    
    @staticmethod
    def is_expensive(price):
        return price > 50000