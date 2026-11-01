TWO_POINT_VALUE = 2
THREE_POINT_VALUE = 3
MVP_POINTS_THRESHOLD = 30


class BasketballPlayer:
    total_players = 0

    def __init__(self, name, two_pointers, three_pointers):
        self.name = name
        self.two_pointers = two_pointers
        self.three_pointers = three_pointers
        self.total_points = self.calculate_total_points(two_pointers, three_pointers)
        BasketballPlayer.total_players += 1

    @staticmethod
    def calculate_total_points(two_pointers, three_pointers):
        return (two_pointers * TWO_POINT_VALUE) + (three_pointers * THREE_POINT_VALUE)

    def shot_count(self):
        return self.two_pointers + self.three_pointers

    def get_player_stats(self):
        return f"Player: {self.name} | Shots: {self.shot_count()} | Score: {self.total_points}"

    @classmethod
    def get_team_size(cls):
        return f"Team report: now on our team {cls.total_players} players"

    @classmethod
    def from_string(cls, data_string):
        name, twos, threes = data_string.split('-')
        return cls(name, int(twos), int(threes))

    @staticmethod
    def is_mvp_level(points):
        if points >= MVP_POINTS_THRESHOLD:
            return "Yes, MVP level!"
        else:
            return "Good, but needs more practice."


player1 = BasketballPlayer("Nazar", 15, 2)
player2 = BasketballPlayer("Taras", 8, 12)

player3 = BasketballPlayer.from_string("LeBron-12-4")

print(player1.get_player_stats())
print(player2.get_player_stats())
print(player3.get_player_stats())

print("-" * 20)
print(BasketballPlayer.get_team_size())

print("-" * 20)
print(f"Is Nazar MVP? - {BasketballPlayer.is_mvp_level(player1.total_points)}")
print(f"Is Taras MVP? - {BasketballPlayer.is_mvp_level(player2.total_points)}")
