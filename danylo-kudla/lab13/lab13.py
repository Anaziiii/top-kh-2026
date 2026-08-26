from abc  import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def set_channel(self, channel):
        pass

class TV(Device):
    def turn_on(self):
        print("Телевізор увімкнений")

    def turn_off(self):
        print("Телевізор вимкнений")

    def set_channel(self, channel):
        print(f"Телевізор на каналі {channel}")

class Radio(Device):
    def turn_on(self):
        print("Радіо увімкнено")

    def turn_off(self):
        print("Радіо вимкнено")

    def set_channel(self, channel):
        print(f"Радіо на частоті{channel}")

class RemoteControl:
    def __init__(self, device):
        self.device = device

    def power_on(self):
        self.device.turn_on()

    def power_off(self):
        self.device.turn_off()

    def channel(self, number):
        self.device.set_channel(number)

class AddRemoteControl(RemoteControl):
    def mute(self):
        print("Звук вимкнено")


tv = TV()
radio = Radio()

basic_remote = RemoteControl(tv)
basic_remote.power_on()
basic_remote.channel(5)

adv_remote = AddRemoteControl(radio)
adv_remote.power_on()
adv_remote.mute()