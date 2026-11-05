class PaymentStrategy:
    def pay(self, amount: int) -> str:
        pass


class CardPayment(PaymentStrategy):
    def pay(self, amount: int) -> str:
        return f"Оплачено {amount} грн банківською карткою."


class CryptoPayment(PaymentStrategy):
    def pay(self, amount: int) -> str:
        return f"Оплачено {amount} грн криптовалютою."


class ShoppingCart:
    def __init__(self, amount: int, strategy: PaymentStrategy):
        self.amount = amount
        self.strategy = strategy

    def checkout(self):
        return self.strategy.pay(self.amount)


if __name__ == "__main__":
    cart = ShoppingCart(500, CardPayment())
    print(cart.checkout())

    cart.strategy = CryptoPayment()
    print(cart.checkout())