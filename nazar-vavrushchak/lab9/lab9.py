class BasketballPlayer:
    total_players = 0

    def __init__(self, name, two_pointers, three_pointers):
        self.name = name
        self.two_pointers = two_pointers
        self.three_pointers = three_pointers
        self.total_points = (self.two_pointers * 2) + (self.three_pointers * 3)
        BasketballPlayer.total_players += 1

    def get_role_description(self):
        return f"{self.name} - a regular team player."

    def __str__(self):
        return f"Player: {self.name} | Total Score: {self.total_points}"

    def __add__(self, other):
        return self.total_points + other.total_points

    def __gt__(self, other):
        return self.total_points > other.total_points

class Captain(BasketballPlayer):
    def __init__(self, name, two_pointers, three_pointers, experience_years):
        super().__init__(name, two_pointers, three_pointers)
        self.experience_years = experience_years

    def get_role_description(self):
        return f" {self.name} - Team Captain with {self.experience_years} years of experience!"

class Rookie(BasketballPlayer):
    def __init__(self, name, two_pointers, three_pointers, potential_level):
        super().__init__(name, two_pointers, three_pointers)
        self.potential_level = potential_level

    def get_role_description(self):
        return f" {self.name} - Promising rookie (potential: {self.potential_level})."

player1 = BasketballPlayer("Nazar", 10, 2)
captain1 = Captain("Michael", 20, 5, 10)
rookie1 = Rookie("Taras", 5, 1, 90)

print("--- 1 & 2. Polymorphism and Method Overriding ---")
team = [player1, captain1, rookie1]

for person in team:
    print(person.get_role_description())

print("\n--- 3. Magic Methods ---")

print("Testing __str__:")
print(player1)
print(captain1)

print("\nTesting __add__ (+ operator):")
combined_score = player1 + captain1
print(f"Combined score of {player1.name} and {captain1.name} is {combined_score}")

print("\nTesting __gt__ (> operator):")
if captain1 > player1:
    print(f"{captain1.name} scored more points than {player1.name}!")
else:
    print(f"{player1.name} scored more points than {captain1.name}!")