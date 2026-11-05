class BadShoppingCart:
    def __init__(self, amount: int):
        self.amount = amount

    def checkout(self, payment_type: str):
        if payment_type == "card":
            return f"Оплачено {self.amount} грн банківською карткою."
        elif payment_type == "crypto":
            return f"Оплачено {self.amount} грн криптовалютою."
        else:
            return "Невідомий спосіб оплати!"


if __name__ == "__main__":
    cart = BadShoppingCart(500)
    print(cart.checkout("card"))
    print(cart.checkout("crypto"))