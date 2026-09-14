from abc import ABC, abstractmethod

# 1. Інтерфейс стратегії
class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, amount: float) -> float:
        pass

# 2. Конкретні реалізації стратегій
class NoDiscount(DiscountStrategy):
    def apply_discount(self, amount: float) -> float:
        return amount

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent: float):
        self.percent = percent

    def apply_discount(self, amount: float) -> float:
        return amount * (1 - self.percent / 100)

class FixedDiscount(DiscountStrategy):
    def __init__(self, discount_amount: float):
        self.discount_amount = discount_amount

    def apply_discount(self, amount: float) -> float:
        return max(0.0, amount - self.discount_amount)

# 3. Контекст, який використовує обрану стратегію
class Order:
    def __init__(self, total_price: float, discount_strategy: DiscountStrategy):
        self.total_price = total_price
        self.discount_strategy = discount_strategy

    def calculate_final_price(self) -> float:
        return self.discount_strategy.apply_discount(self.total_price)

# Використання
if __name__ == "__main__":
    raw_price = 1000.0

    # Без знижки
    order1 = Order(raw_price, NoDiscount())
    print(f"Ціна без знижки: {order1.calculate_final_price()} грн")

    # Знижка 15%
    order2 = Order(raw_price, PercentageDiscount(15))
    print(f"Ціна зі знижкою 15%: {order2.calculate_final_price()} грн")

    # Фіксована знижка 200 грн
    order3 = Order(raw_price, FixedDiscount(200))
    print(f"Ціна з фіксованою знижкою 200 грн: {order3.calculate_final_price()} грн")