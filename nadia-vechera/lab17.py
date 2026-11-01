import unittest


# 1. Функції, які підлягають тестуванню
def add(a, b):
  """Повертає суму двох чисел."""
  return a + b


def is_even(number):
  """Повертає True, якщо число парне, і False в іншому випадку."""
  return number % 2 == 0


# 2. Клас для написання unit-тестів
class TestMathAndLogicFunctions(unittest.TestCase):

  def test_add(self):
    # Перевірка коректності додавання
    self.assertEqual(add(3, 5),)
    self.assertEqual(add(-1, 1), 0)
    self.assertEqual(add(-5, -5), -10)

  def test_is_even(self):
    # Перевірка функції визначення парності чисел
    self.assertTrue(is_even(4))
    self.assertTrue(is_even(0))
    self.assertFalse(is_even(3))
    self.assertFalse(is_even(-5))


# 3. Точка входу для запуску тестів
if __name__ == "__main__":
  unittest.main()