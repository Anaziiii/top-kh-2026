class BasketballPlayer:
    total_players = 0

    def __init__(self, name, two_pointers, three_pointers, jersey_number):
        self.name = name
        self.two_pointers = two_pointers
        self.three_pointers = three_pointers
        self.jersey_number = jersey_number

        BasketballPlayer.total_players += 1

    @property
    def total_points(self):
        return (self.two_pointers * 2) + (self.three_pointers * 3)

    @property
    def jersey_number(self):
        return self._jersey_number

    @jersey_number.setter
    def jersey_number(self, value):
        if not isinstance(value, int) or value <= 0:
            print(f"Error: Jersey number must be a positive integer! Setting to default 0.")
            self._jersey_number = 0
        else:
            self._jersey_number = value

    @jersey_number.deleter
    def jersey_number(self):
        print(f"Jersey number {self._jersey_number} has been released. {self.name} returned the uniform.")
        self._jersey_number = None

print("--- 1. Testing @property (Dynamic Calculation) ---")
player1 = BasketballPlayer("Nazar", 10, 2, 7)
print(f"Player: {player1.name} | Initial Score: {player1.total_points}")

player1.two_pointers += 5
print(f"Score after 5 more two-pointers: {player1.total_points}")

print("\n--- 2. Testing Setter and Validation ---")
print(f"Current jersey number: {player1.jersey_number}")

player1.jersey_number = 23
print(f"New jersey number: {player1.jersey_number}")

player1.jersey_number = -5

print("\n--- 3. Testing Deleter ---")
del player1.jersey_number
print(f"Jersey number after deletion: {player1.jersey_number}")