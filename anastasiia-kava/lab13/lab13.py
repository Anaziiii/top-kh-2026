class PhoneSpecs:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = float(price)
class FinancialSystem:
    def __init__(self, exchange_rate=42.0, tax_rate=0.05):
        self.exchange_rate = exchange_rate
        self.tax_rate = tax_rate
    def to_dollars(self, price_uah):
        return price_uah / self.exchange_rate
    def apply_tax(self, price_uah):
        return price_uah * (1 + self.tax_rate)
class AudioSystem:
    def play_sound(self, sound_type):
        if sound_type == "ring":
            return "Beep! Beep!"
        return "Unknown sound"
class PhoneFacade:
    def __init__(self, brand, model, price):

        self.specs = PhoneSpecs(brand, model, price)
        self.finance = FinancialSystem()
        self.audio = AudioSystem()

    def ring(self):
        sound = self.audio.play_sound("ring")
        return f"{self.specs.brand} {self.specs.model}: {sound}"

    def apply_tax(self):
        self.specs.price = self.finance.apply_tax(self.specs.price)

    def info(self):
        price_in_usd = self.finance.to_dollars(self.specs.price)
        return (f"Brand: {self.specs.brand}, Model: {self.specs.model}, "
                f"Price: {self.specs.price:.2f} грн. Долар: {price_in_usd:.2f}")

if __name__ == "__main__":
    iphone_15 = PhoneFacade("Apple", "iPhone 15", 45000)
    
    print("Дзвінок: ", iphone_15.ring())
    print("Інфо:    ", iphone_15.info())
    
    iphone_15.apply_tax()
    print("Податок: ", iphone_15.info())