import unittest
from main import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_case(self):
        result = self.solution.twoSum([2, 7, 11, 15], 9)
        self.assertIn(result, [[0, 1], [1, 0]])

    def test_multiple_possible_pairs(self):
        result = self.solution.twoSum([3, 2, 4, 1, 5], 6)
        self.assertEqual(result[0] + result[1], 6)

    def test_negative_numbers(self):
        result = self.solution.twoSum([-1, -2, -3, -4, -5], -8)
        self.assertIn(result, [[2, 4], [4, 2]])

    def test_zero_target(self):
        result = self.solution.twoSum([1, -1, 2, 3], 0)
        self.assertIn(result, [[0, 1], [1, 0]])

    def test_duplicate_numbers(self):
        result = self.solution.twoSum([3, 3, 4, 5], 6)
        self.assertIn(result, [[0, 1], [1, 0]])

    def test_no_solution(self):
        result = self.solution.twoSum([1, 2, 3, 4], 10)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
