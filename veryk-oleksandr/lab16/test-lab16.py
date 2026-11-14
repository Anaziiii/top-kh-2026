
import unittest
from lab16 import MediaContent


class TestMediaContent(unittest.TestCase):

    def setUp(self):
        self.movie = MediaContent("Інтерстеллар", 2014)

    def test_initial_data(self):
        self.assertEqual(self.movie.title, "Інтерстеллар")
        self.assertEqual(self.movie.year, 2014)

    def test_add_rating(self):
        self.movie.add_rating(8)
        self.assertEqual(self.movie.ratings, [8])

    def test_invalid_rating(self):
        with self.assertRaises(ValueError):
            self.movie.add_rating(11)

    def test_average_rating(self):
        self.movie.add_rating(8)
        self.movie.add_rating(10)
        self.assertEqual(self.movie.average_rating, 9)


if __name__ == "__main__":
    unittest.main()
