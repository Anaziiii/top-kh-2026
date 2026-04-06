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

    def get_team_size_info(self):
        return f"Player {self.name} reports: now on our team {BasketballPlayer.total_players} players"

player1 = BasketballPlayer("Nazar", 15, 2)
print(player1.get_team_size_info())

player2 = BasketballPlayer("Taras", 8, 12)

print(player1.get_team_size_info())
print(player2.get_team_size_info())

print(f"Total number of objects created: {BasketballPlayer.total_players}")