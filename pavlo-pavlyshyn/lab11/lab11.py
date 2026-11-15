from abc import ABC, abstractmethod


class Dog:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


# Базовий клас раціону. Нові раціони додаються як нові класи,
# а код розплідника при цьому не змінюється (принцип OCP).
class FeedingPlan(ABC):
    title = ""

    @abstractmethod
    def daily_portion(self, dog):
        pass


class PuppyPlan(FeedingPlan):
    title = "Цуценя"

    def daily_portion(self, dog):
        return dog.weight * 60


class AdultPlan(FeedingPlan):
    title = "Доросла собака"

    def daily_portion(self, dog):
        return dog.weight * 25


class SeniorPlan(FeedingPlan):
    title = "Літня собака"

    def daily_portion(self, dog):
        return dog.weight * 18


class Kennel:
    def __init__(self):
        self.residents = []

    def add(self, dog, plan):
        self.residents.append((dog, plan))

    def print_menu(self):
        total = 0
        for dog, plan in self.residents:
            portion = plan.daily_portion(dog)
            total += portion
            print(f"{dog.name} ({plan.title}, {dog.weight} кг) - {portion} г корму на день")
        print(f"Разом на день: {total / 1000} кг")


kennel = Kennel()
kennel.add(Dog("Барс", 32), AdultPlan())
kennel.add(Dog("Дуна", 6), PuppyPlan())
kennel.add(Dog("Рекс", 28), SeniorPlan())
kennel.print_menu()
