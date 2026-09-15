from abc import ABC, abstractmethod

# 1. Інтерфейс стратегії
class ShippingStrategy(ABC):
    @abstractmethod
    def calculate_cost(self, weight: float) -> float:
        pass

# 2. Конкретні стратегії
class CourierDelivery(ShippingStrategy):
    def calculate_cost(self, weight: float) -> float:
        return weight * 15.0 + 50.0  # Базова ставка + за вагу

class PostalDelivery(ShippingStrategy):
    def calculate_cost(self, weight: float) -> float:
        return weight * 8.0

class PickupDelivery(ShippingStrategy):
    def calculate_cost(self, weight: float) -> float:
        return 0.0  # Безкоштовно

# 3. Контекст, що використовує стратегію
class OrderCalculator:
    def __init__(self, strategy: ShippingStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: ShippingStrategy):
        self.strategy = strategy

    def get_total_shipping(self, weight: float) -> float:
        return self.strategy.calculate_cost(weight)

# --- Використання ---
weight = 3.5  # кг

calc = OrderCalculator(CourierDelivery())
print(f"Кур'єр: {calc.get_total_shipping(weight)} грн")  # 102.5 грн

# Динамічна зміна поведінки
calc.set_strategy(PostalDelivery())
print(f"Пошта: {calc.get_total_shipping(weight)} грн")    # 28.0 грн