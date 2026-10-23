from abc import ABC, abstractmethod

class ATCMediator(ABC):
    @abstractmethod
    def request_landing(self, airplane):
        pass
    @abstractmethod
    def notify_runway_cleared(self):
        pass

class Airplane:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    def land(self):
        self.mediator.notify_runway_cleared()

    def wait_in_air(self):
        pass

class Tower(ATCMediator):
    def __init__(self):
        self._is_runway_free = True
        self._waiting_queue = []

    def request_landing(self, airplane):
        if self._is_runway_free:
            self._is_runway_free = False
            airplane.land()
        else:
            self._waiting_queue.append(airplane)
            airplane.wait_in_air()

    def notify_runway_cleared(self):
        self._is_runway_free = True
        if self._waiting_queue:
            next_airplane = self._waiting_queue.pop(0)
            self.request_landing(next_airplane)