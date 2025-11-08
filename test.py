import unittest

class TestSum(unittest.TestCase):
    def test_sum(self):
        # Falla: sum() espera un iterable, no dos enteros
        self.assertEqual(sum(1, 2), 3)

if __name__ == '__main__':
    unittest.main()
