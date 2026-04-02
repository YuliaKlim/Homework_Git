import unittest
from homework_12 import my_sum, arithmetic_mean, my_string, find_substring, list_sum_even

class MyTenTestCases(unittest.TestCase):
    def test_my_sum(self):
        result = my_sum(2, 3)
        self.assertEqual(result, 5)

    def test_my_sum_int(self):
        result = my_sum(4, 5)
        self.assertIsInstance(result, int)

    def test_arithmetic_mean(self):
        result = arithmetic_mean([1, 2, 3, 4, 5])
        self.assertEqual(result, 3)

    def test_arithmetic_mean_float(self):
        result = arithmetic_mean([1, 2, 3, 4, 5])
        self.assertIsInstance(result, float)

    def test_my_string(self):
        result = my_string('hello world')
        self.assertEqual(result, 'dlrow olleh')

    def test_find_substring(self):
        index_str = find_substring('I want a 100 mark', '100')
        self.assertGreater(index_str, -1)

    def test_find_substring_number_index(self):
        index_str = find_substring('I want a 100 mark', '100')
        self.assertEqual(index_str, 9)

    def test_not_found_substring(self):
        index_str = find_substring('I want a 100 mark', '50')
        self.assertLess(index_str, 0)

    def test_not_found_substring_equal(self):
        index_str = find_substring('I want a 100 mark', '50')
        self.assertEqual(index_str, -1)

    def test_list_sum_even(self):
        result = list_sum_even([12, 21, 30, 45, 52,])
        self.assertEqual(result, 94)

if __name__ == '__main__':
    unittest.main(verbosity=2)