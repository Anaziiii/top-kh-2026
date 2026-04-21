class BasketballPlayer:

    def __init__(self, name, two_pointers, three_pointers):
        self.name = name
        self.two_pointers = two_pointers
        self.three_pointers = three_pointers

        self.total_points = (self.two_pointers * 2) + (self.three_pointers * 3)

    def get_player_stats(self):
        return f"Player: {self.name} | Shots: {self.two_pointers + self.three_pointers} | Score: {self.total_points}"

player1 = BasketballPlayer("Nazar", 15, 2)
player2 = BasketballPlayer("Taras", 8, 12)

print(player1.get_player_stats())
print(player2.get_player_stats())

print(BasketballPlayer.get_player_stats(player1))
print(BasketballPlayer.get_player_stats(player2))