from abc import ABC, abstractmethod

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Feedable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Human(Workable, Feedable):
    def work(self):
        print("Людина працює")

    def eat(self):
        print("Людина їсть")

class Robot(Workable):
    def work(self):
        print("Робот працює")