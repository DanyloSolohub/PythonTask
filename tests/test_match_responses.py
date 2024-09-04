import json
import unittest


class TestMatchResponses(unittest.TestCase):

    def test_gb_holidays(self):
        with open('actual_results/gb_actual_result.txt', 'r') as file:
            actual_results = file.read()
        with open('expected_results/gb_7-7-1992_18-9-1992.txt', 'r') as file:
            expected_results = file.read()
        self.assertEqual(actual_results, expected_results)

    def test_ua_holidays(self):
        with open('actual_results/ua_actual_result.txt', 'r') as file:
            actual_results = file.read()
        with open('expected_results/ua_7-7-1992_18-9-1992.txt', 'r') as file:
            expected_results = file.read()
        self.assertEqual(actual_results, expected_results)

    def test_us_holidays(self):
        with open('actual_results/us_actual_result.txt', 'r') as file:
            actual_results = file.read()
        with open('expected_results/us_7-7-1992_18-9-1992.txt', 'r') as file:
            expected_results = file.read()
        self.assertEqual(actual_results, expected_results)


if __name__ == '__main__':
    unittest.main()
