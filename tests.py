import unittest


class Numerics:

    def __init__(self):
        pass

    def add(self, num1, num2):
        """
        Add two numbers
        """

        return num1 + num2


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        num = Numerics()
        self.assertEqual(num.add(5, 5), 10)

    def test_isupper(self):
        num = Numerics()
        self.assertTrue(1 == num.add(1, 0))
        self.assertFalse(0 == num.add(1, 0))


if __name__ == '__main__':
    unittest.main()
