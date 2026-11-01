import unittest

class TestDateHelper(unittest.TestCase):
    def test_parse_dates_success(self):
        dates, error = DateHelper.parse_rental_dates("2026.10.20","2026.10.22")
        self.assertIsNone(error)
        self.assertEqual(dates[0], date(2026, 10, 20))
        self.assertEqual(dates[1], date(2026, 10, 22))

    def test_parse_dates_invalid_format(self):
        dates, error = DateHelper.parse_rental_dates("20.10.2026", "2026.10.22")
        self.assertIsNone(dates)
        self.assertIn("Неправильний формат", error)