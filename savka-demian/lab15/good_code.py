class InvoiceManager:
    def print_header(self):
        print("РАХУНОК НА ОПЛАТУ")

    def calculate_total(self, items: list) -> float:
        return sum(items)

    def print_invoice(self, customer_name: str, items: list):
        self.print_header()
        total = self.calculate_total(items)
        print(f"Клієнт: {customer_name}")
        print(f"Сума до сплати: {total} грн")


if __name__ == "__main__":
    manager = InvoiceManager()
    manager.print_invoice("Олександр", [250, 150, 100])