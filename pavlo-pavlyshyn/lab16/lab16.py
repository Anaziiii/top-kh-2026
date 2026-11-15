class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed


class Shelter:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dogs = []

    def take_in(self, dog):
        if len(self.dogs) >= self.capacity:
            raise ValueError("У притулку немає вільних місць")
        if self.find(dog.name) is not None:
            raise ValueError("Собака з такою кличкою вже є")
        self.dogs.append(dog)

    def find(self, name):
        for dog in self.dogs:
            if dog.name == name:
                return dog
        return None

    def give_away(self, name):
        dog = self.find(name)
        if dog is None:
            raise ValueError("Такої собаки немає в притулку")
        self.dogs.remove(dog)
        return dog

    def free_places(self):
        return self.capacity - len(self.dogs)

    def by_breed(self, breed):
        return [dog for dog in self.dogs if dog.breed == breed]

    def average_age(self):
        if not self.dogs:
            return 0
        return sum(dog.age for dog in self.dogs) / len(self.dogs)
