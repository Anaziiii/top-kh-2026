from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str):
        self.card_number = card_number

    def pay(self, amount: float):
        print(f"Processing ${amount} payment using Credit Card ending in {self.card_number[-4:]}.")


class PayPalPayment(PaymentStrategy):
    def __init__(self, email: str):
        self.email = email

    def pay(self, amount: float):
        print(f"Processing ${amount} payment via PayPal account: {self.email}.")


class CryptoPayment(PaymentStrategy):
    def __init__(self, wallet_address: str):
        self.wallet_address = wallet_address

    def pay(self, amount: float):
        print(f"Processing ${amount} payment via Crypto wallet: {self.wallet_address}.")

class ShoppingCart:
    def __init__(self):
        self.amount = 0
        self._payment_strategy = None

    def add_item(self, price: float):
        self.amount += price
        print(f"Added item worth ${price}. Total: ${self.amount}.")

    def set_payment_strategy(self, strategy: PaymentStrategy):
        self._payment_strategy = strategy

    def checkout(self):
        if not self._payment_strategy:
            print("Error: Payment strategy not set!")
            return

        self._payment_strategy.pay(self.amount)
        self.amount = 0

cart = ShoppingCart()
cart.add_item(150.00)
cart.add_item(50.00)

print("\n--- Testing Credit Card Strategy ---")
cart.set_payment_strategy(CreditCardPayment("1234-5678-9012-3456"))
cart.checkout()

print("\n--- Testing PayPal Strategy ---")
cart.add_item(75.50)
cart.set_payment_strategy(PayPalPayment("nazar@example.com"))
cart.checkout()