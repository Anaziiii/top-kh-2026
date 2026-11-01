import unittest

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


class BasketballPlayerTests(unittest.TestCase):
    def setUp(self):
        BasketballPlayer.total_players = 0

    def test_calculate_total_points(self):
        self.assertEqual(BasketballPlayer.calculate_total_points(15, 2), 36)
        self.assertEqual(BasketballPlayer.calculate_total_points(8, 12), 52)
        self.assertEqual(BasketballPlayer.calculate_total_points(12, 4), 36)

    def test_nazar_shot_count_and_stats(self):
        player = BasketballPlayer("Nazar", 15, 2)
        self.assertEqual(player.shot_count(), 17)
        self.assertEqual(
            player.get_player_stats(),
            "Player: Nazar | Shots: 17 | Score: 36",
        )

    def test_from_string_lebron(self):
        player = BasketballPlayer.from_string("LeBron-12-4")
        self.assertEqual(player.name, "LeBron")
        self.assertEqual(player.total_points, 36)

    def test_is_mvp_level_boundary(self):
        self.assertEqual(BasketballPlayer.is_mvp_level(30), "Yes, MVP level!")
        self.assertEqual(
            BasketballPlayer.is_mvp_level(29),
            "Good, but needs more practice.",
        )

    def test_team_size_after_one_player(self):
        BasketballPlayer("Nazar", 15, 2)
        self.assertIn("1", BasketballPlayer.get_team_size())
        self.assertEqual(
            BasketballPlayer.get_team_size(),
            "Team report: now on our team 1 players",
        )


if __name__ == "__main__":
    unittest.main()
