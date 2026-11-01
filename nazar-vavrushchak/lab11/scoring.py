TWO_POINT_VALUE = 2
THREE_POINT_VALUE = 3


class ScoreCalculator:
    @staticmethod
    def calculate_total_points(two_pointers, three_pointers):
        return (two_pointers * TWO_POINT_VALUE) + (three_pointers * THREE_POINT_VALUE)

    @staticmethod
    def shot_count(two_pointers, three_pointers):
        return two_pointers + three_pointers


if __name__ == "__main__":
    points = ScoreCalculator.calculate_total_points(15, 2)
    shots = ScoreCalculator.shot_count(15, 2)
    print(f"Nazar points: {points}")
    print(f"Nazar shots: {shots}")
