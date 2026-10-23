from abc import ABC, abstractmethod

# 1. Базовий компонент (інтерфейс кави)
class Coffee(ABC):
    @abstractmethod
    def get_cost(self) -> float:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass


# 2. Конкретний компонент (основа)
class SimpleCoffee(Coffee):
    def get_cost(self) -> float:
        return 30.0

    def get_description(self) -> str:
        return "Звичайна кава"


# 3. Базовий декоратор
class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    def get_cost(self) -> float:
        return self._coffee.get_cost()

    def get_description(self) -> str:
        return self._coffee.get_description()


# 4. Конкретні декоратори (додатки)
class MilkDecorator(CoffeeDecorator):
    def get_cost(self) -> float:
        return self._coffee.get_cost() + 10.0

    def get_description(self) -> str:
        return self._coffee.get_description() + ", молоко"


class SugarDecorator(CoffeeDecorator):
    def get_cost(self) -> float:
        return self._coffee.get_cost() + 5.0

    def get_description(self) -> str:
        return self._coffee.get_description() + ", цукор"


class WhipDecorator(CoffeeDecorator):
    def get_cost(self) -> float:
        return self._coffee.get_cost() + 15.0

    def get_description(self) -> str:
        return self._coffee.get_description() + ", збиті вершки"


# --- Приклад використання ---
if __name__ == "__main__":
    # Звичайна кава
    coffee = SimpleCoffee()
    print(f"{coffee.get_description()} → {coffee.get_cost()} грн")

    # Кава + молоко
    coffee_with_milk = MilkDecorator(coffee)
    print(f"{coffee_with_milk.get_description()} → {coffee_with_milk.get_cost()} грн")

    # Кава + молоко + цукор
    coffee_milk_sugar = SugarDecorator(coffee_with_milk)
    print(f"{coffee_milk_sugar.get_description()} → {coffee_milk_sugar.get_cost()} грн")

    # Кава + молоко + цукор + збиті вершки
    luxury_coffee = WhipDecorator(coffee_milk_sugar)
    print(f"{luxury_coffee.get_description()} → {luxury_coffee.get_cost()} грн")