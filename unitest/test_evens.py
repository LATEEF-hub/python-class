import unittest
from evens import even_num_of_evens

class TestEvens(unittest.TestCase):
    def test_throw_error_if_is_not_even(self):
        self.assertRaises(TypeError, even_num_of_evens, 4)


    # def test_function_returns_True(self):
    #     self.assertTrue(even_num_of_evens([]))
if __name__ == '__main__':
   unittest.main()