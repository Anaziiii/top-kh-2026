# Неправильно: один клас і рахує очки, і форматує звіт.
# Зміна правила нарахування і зміна тексту статистики чіпають той самий клас.

TWO_POINT_VALUE = 2
THREE_POINT_VALUE = 3


class PlayerMixed:
    @staticmethod
    def calculate_total_points(two_pointers, three_pointers):
        return (two_pointers * TWO_POINT_VALUE) + (three_pointers * THREE_POINT_VALUE)

    @staticmethod
    def format_stats(name, two_pointers, three_pointers):
        shots = two_pointers + three_pointers
        points = PlayerMixed.calculate_total_points(two_pointers, three_pointers)
        return f"Player: {name} | Shots: {shots} | Score: {points}"


if __name__ == "__main__":
    print(PlayerMixed.format_stats("Nazar", 15, 2))
