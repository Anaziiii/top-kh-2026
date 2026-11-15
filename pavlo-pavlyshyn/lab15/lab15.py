# Код ПІСЛЯ рефакторингу. Початковий варіант наведено у звіті lab15.md

SMALL_DOG_MAX_WEIGHT = 10
MEDIUM_DOG_MAX_WEIGHT = 25

SMALL_DOG_RATE = 250
MEDIUM_DOG_RATE = 350
LARGE_DOG_RATE = 450

LONG_STAY_DAYS = 7
LONG_STAY_DISCOUNT = 0.1
NO_VACCINE_FEE = 200


def day_rate(weight):
    if weight < SMALL_DOG_MAX_WEIGHT:
        return SMALL_DOG_RATE
    if weight < MEDIUM_DOG_MAX_WEIGHT:
        return MEDIUM_DOG_RATE
    return LARGE_DOG_RATE


def is_long_stay(days):
    return days >= LONG_STAY_DAYS


def long_stay_discount(price, days):
    if is_long_stay(days):
        return price * LONG_STAY_DISCOUNT
    return 0


def vaccine_fee(vaccinated):
    if vaccinated:
        return 0
    return NO_VACCINE_FEE


def stay_price(weight, days, vaccinated):
    price = day_rate(weight) * days
    price -= long_stay_discount(price, days)
    price += vaccine_fee(vaccinated)
    return price


def print_bill(name, weight, days, vaccinated):
    print(f"{name}: {days} дн. у готелі - {stay_price(weight, days, vaccinated)} грн")


print_bill("Дуна", 6, 3, True)
print_bill("Барс", 32, 10, True)
print_bill("Сірко", 18, 2, False)
