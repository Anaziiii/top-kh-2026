class PlayerReport:
    @staticmethod
    def format_stats(name, shots, points):
        return f"Player: {name} | Shots: {shots} | Score: {points}"


if __name__ == "__main__":
    print(PlayerReport.format_stats("Nazar", 17, 36))
