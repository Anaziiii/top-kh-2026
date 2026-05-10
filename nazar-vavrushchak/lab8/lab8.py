class BasketballPlayer:
    total_players = 0

    def __init__(self, name, two_pointers, three_pointers):
        self.name = name
        self.two_pointers = two_pointers
        self.three_pointers = three_pointers
        self.total_points = (self.two_pointers * 2) + (self.three_pointers * 3)
        BasketballPlayer.total_players += 1

    def get_player_stats(self):
        return f"Player: {self.name} | Shots: {self.two_pointers + self.three_pointers} | Score: {self.total_points}"

class Captain(BasketballPlayer):
    def __init__(self, name, two_pointers, three_pointers, experience_years):
        super().__init__(name, two_pointers, three_pointers)
        self.experience_years = experience_years

    def motivate_rookie(self, rookie_player):
        print(f"Captain {self.name} encourages the rookie:")
        print(f" - 'Come on, {rookie_player.name}! You can do better!'")
        print(f" - Rookie's current stats: {rookie_player.get_player_stats()}")

class Rookie(BasketballPlayer):
    def __init__(self, name, two_pointers, three_pointers, potential_level):
        super().__init__(name, two_pointers, three_pointers)
        self.potential_level = potential_level

    def show_potential(self):
        return f"Rookie {self.name} has a potential level of {self.potential_level}/100."

print("--- Object Creation and Inheritance ---")
captain1 = Captain("Nazar", 20, 5, 7)
rookie1 = Rookie("Taras", 5, 1, 85)

print(captain1.get_player_stats())
print(rookie1.show_potential())

print("\n--- Class Interaction (Point 3) ---")
captain1.motivate_rookie(rookie1)

print("\n--- Type Checking: isinstance and issubclass (Point 4) ---")
print(f"Is captain1 an instance of the Captain class? -> {isinstance(captain1, Captain)}")
print(f"Is captain1 an instance of the parent BasketballPlayer? -> {isinstance(captain1, BasketballPlayer)}")

print(f"Is Rookie a subclass of BasketballPlayer? -> {issubclass(Rookie, BasketballPlayer)}")
print(f"Is BasketballPlayer a subclass of Captain? -> {issubclass(BasketballPlayer, Captain)}")