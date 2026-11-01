class Light:
    def turn_on(self):
        return "Light is turned on."

    def turn_off(self):
        return "Light is turned off."


class TV:
    def turn_on(self):
        return "TV is turned on. News channel is on."

    def turn_off(self):
        return "TV is turned off."

class AirConditioner:
    def turn_on(self):
        return "Air conditioner is turned on. Temperature: 22°C."

    def turn_off(self):
        return "Air conditioner is turned off."

class SmartHomeFacade:
    def __init__(self):
        self.light = Light()
        self.tv = TV()
        self.ac = AirConditioner()

    def good_morning(self):
        print("\n--- Starting scenario: Good Morning ---")
        print(self.light.turn_on())
        print(self.tv.turn_on())
        print(self.ac.turn_on())

    def leave_home(self):
        print("\n--- Starting scenario: Leaving Home ---")
        print(self.light.turn_off())
        print(self.tv.turn_off())
        print(self.ac.turn_off())

smart_home = SmartHomeFacade()

smart_home.good_morning()

smart_home.leave_home()