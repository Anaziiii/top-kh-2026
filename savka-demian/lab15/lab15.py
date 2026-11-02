def print_invoice(customer_name, items):
    print("РАХУНОК НА ОПЛАТУ")
    total = sum(items)
    print(f"Клієнт: {customer_name}")
    print(f"Сума до сплати: {total} грн")


def print_header():
    print("РАХУНОК НА ОПЛАТУ")

def print_invoice_refactored(customer_name, items):
    print_header()
    print(f"Клієнт: {customer_name}")
    print(f"Сума до сплати: {sum(items)} грн")