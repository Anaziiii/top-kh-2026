from abc import ABC, abstractmethod


class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f"{self.name} - {self.age} - {self.breed}"


class Subscriber(ABC):
    @abstractmethod
    def update(self, event, dog):
        pass


class Volunteer(Subscriber):
    def __init__(self, name):
        self.name = name

    def update(self, event, dog):
        if event == "arrived":
            print(f"  Волонтер {self.name}: вигуляю новеньку собаку {dog.name}")
        elif event == "adopted":
            print(f"  Волонтер {self.name}: радію за {dog.name}!")


class Vet(Subscriber):
    def update(self, event, dog):
        if event == "arrived":
            print(f"  Ветеринар: записую {dog.name} на огляд")


class BreedFan(Subscriber):
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def update(self, event, dog):
        if event == "arrived" and dog.breed == self.breed:
            print(f"  {self.name}: з'явилась {self.breed}, їду знайомитись з {dog.name}")


# Видавець: зберігає підписників і повідомляє їх про події
class Shelter:
    def __init__(self):
        self.dogs = []
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify(self, event, dog):
        for subscriber in self.subscribers:
            subscriber.update(event, dog)

    def take_in(self, dog):
        self.dogs.append(dog)
        print(f"До притулку прибула собака: {dog}")
        self.notify("arrived", dog)

    def give_away(self, dog):
        self.dogs.remove(dog)
        print(f"Собаку забрали додому: {dog}")
        self.notify("adopted", dog)


shelter = Shelter()
olena = Volunteer("Олена")
fan = BreedFan("Андрій", "Лабрадор")

shelter.subscribe(olena)
shelter.subscribe(Vet())
shelter.subscribe(fan)

bars = Dog("Барс", 5, "Вівчарка")
luna = Dog("Луна", 2, "Лабрадор")

shelter.take_in(bars)
shelter.take_in(luna)

shelter.unsubscribe(fan)
shelter.give_away(luna)
