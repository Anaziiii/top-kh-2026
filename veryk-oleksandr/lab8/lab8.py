class House:
    def __init__(self, address, price, area):
        self.address = address
        self.price = price
        self.area = area

    def get_full_info(self):
        return f"{self.address} | {self.price} | {self.area}"


class Apartment(House):
    def __init__(self, address, price, area, floor):
        super().__init__(address, price, area)
        self.floor = floor

    def get_full_info(self):
        return super().get_full_info() + f" | поверх: {self.floor}"


class Realtor:
    def compare(self, h1, h2):
        if h1.price > h2.price:
            return "Перший дорожчий"
        elif h1.price < h2.price:
            return "Другий дорожчий"
        return "Однакова ціна"