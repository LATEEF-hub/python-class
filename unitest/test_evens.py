import unittest
from evens import even_num_of_evens

class TestEvens(unittest.TestCase):
    #Test to check for even number
    def test_throw_error_if_is_not_even(self):
        self.assertRaises(TypeError, even_num_of_evens, )
        
    
    def test_values_in_list(self):
        #checking if the list entered is an empty list
        self.assertEqual(even_num_of_evens([]), False)
        #checking if the list entered is an 2 value in list
        self.assertEqual(even_num_of_evens([4, 2]), False)
        self.assertEqual(even_num_of_evens([8]), False)
        self.assertEqual(even_num_of_evens([1,3,5]), False)



    # def test_function_returns_True(self):
    #     self.assertTrue(even_num_of_evens([]))
if __name__ == '__main__':
   unittest.main()