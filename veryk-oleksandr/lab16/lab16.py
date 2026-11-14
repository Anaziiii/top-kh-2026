
class MediaContent:
    def __init__(self, title, year):
        self.title = title
        self.year = year
        self.ratings = []

    def add_rating(self, rating):
        if not 1 <= rating <= 10:
            raise ValueError("Оцінка повинна бути від 1 до 10")

        self.ratings.append(rating)

    @property
    def average_rating(self):
        if not self.ratings:
            return 0

        return sum(self.ratings) / len(self.ratings)
