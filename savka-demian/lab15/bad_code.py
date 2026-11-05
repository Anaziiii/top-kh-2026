class BadInvoiceManager:
    def print_invoice(self, customer_name: str, items: list):
        print("РАХУНОК НА ОПЛАТУ")
        total = 0
        for item in items:
            total += item
        print(f"Клієнт: {customer_name}")
        print(f"Сума до сплати: {total} грн")


if __name__ == "__main__":
    manager = BadInvoiceManager()
    manager.print_invoice("Олександр", [250, 150, 100])