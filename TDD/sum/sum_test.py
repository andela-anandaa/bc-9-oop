import unittest

from my_sum import my_sum

class MySumTests(unittest.TestCase):

    def setUp(self):
        # setting up
        self.numbers = [10, 5, 7, 8, 90, 60]

    def test_sum_of_numbers(self):
        '''
        Test sum of digits/numbers
        '''
        result = my_sum(5, 10)
        self.assertEqual(result, 15)
        self.assertEqual(my_sum(10, 15), 25)

    def test_non_numbers(self):
        '''
        Assert throwing of exception when it's a
        a non-number
        '''
        pass


if __name__ == '__main__':
    unittest.main()














