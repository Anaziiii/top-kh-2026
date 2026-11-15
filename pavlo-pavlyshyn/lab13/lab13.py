from abc import ABC, abstractmethod


class Grooming(ABC):
    @abstractmethod
    def price(self):
        pass

    @abstractmethod
    def description(self):
        pass


# Базова послуга, яку можна "обгортати" додатковими
class Wash(Grooming):
    def price(self):
        return 300

    def description(self):
        return "миття"


class Extra(Grooming):
    def __init__(self, service):
        self.service = service

    def price(self):
        return self.service.price()

    def description(self):
        return self.service.description()


class Haircut(Extra):
    def price(self):
        return self.service.price() + 450

    def description(self):
        return self.service.description() + " + стрижка"


class NailTrim(Extra):
    def price(self):
        return self.service.price() + 120

    def description(self):
        return self.service.description() + " + підрізання кігтів"


class EarCleaning(Extra):
    def price(self):
        return self.service.price() + 90

    def description(self):
        return self.service.description() + " + чистка вух"


def print_order(dog_name, service):
    print(f"{dog_name}: {service.description()} = {service.price()} грн")


print_order("Дуна", Wash())
print_order("Барс", Haircut(Wash()))
print_order("Рекс", EarCleaning(NailTrim(Haircut(Wash()))))
