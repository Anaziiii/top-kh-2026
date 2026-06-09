class House:
    currency = "UAH"
    total_houses = 0

    def __init__(self, address, price, area):
        self.address = address
        self.price = price
        self.area = area

        House.total_houses += 1
        self.is_active = True

    def get_price_per_square_meter(self):
        return self.price / self.area

    def get_full_info(self):
        return f"{self.address} | {self.price} {House.currency} | {self.area} м²"

    def delete(self):
        if self.is_active:
            House.total_houses -= 1
            self.is_active = False