import unittest

from lab16 import Dog, Shelter


class TestShelter(unittest.TestCase):
    def setUp(self):
        self.shelter = Shelter(3)
        self.shelter.take_in(Dog("Барс", 5, "Вівчарка"))
        self.shelter.take_in(Dog("Луна", 2, "Лабрадор"))

    def test_free_places(self):
        self.assertEqual(self.shelter.free_places(), 1)

    def test_find_existing_dog(self):
        dog = self.shelter.find("Луна")
        self.assertEqual(dog.breed, "Лабрадор")

    def test_find_missing_dog(self):
        self.assertIsNone(self.shelter.find("Рекс"))

    def test_take_in_duplicate_name(self):
        with self.assertRaises(ValueError):
            self.shelter.take_in(Dog("Барс", 1, "Такса"))

    def test_take_in_when_full(self):
        self.shelter.take_in(Dog("Дуна", 4, "Вівчарка"))
        with self.assertRaises(ValueError):
            self.shelter.take_in(Dog("Рекс", 7, "Боксер"))

    def test_give_away(self):
        dog = self.shelter.give_away("Барс")
        self.assertEqual(dog.name, "Барс")
        self.assertEqual(self.shelter.free_places(), 2)

    def test_give_away_missing_dog(self):
        with self.assertRaises(ValueError):
            self.shelter.give_away("Рекс")

    def test_by_breed(self):
        self.shelter.take_in(Dog("Дуна", 4, "Вівчарка"))
        names = [dog.name for dog in self.shelter.by_breed("Вівчарка")]
        self.assertEqual(names, ["Барс", "Дуна"])

    def test_average_age(self):
        self.assertEqual(self.shelter.average_age(), 3.5)

    def test_average_age_empty_shelter(self):
        self.assertEqual(Shelter(5).average_age(), 0)


if __name__ == "__main__":
    unittest.main()
