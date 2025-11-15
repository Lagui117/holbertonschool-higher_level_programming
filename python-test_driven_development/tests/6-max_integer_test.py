#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_regular_list(self):
        """Test with a regular list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-10, -5, -3, -8]), -3)

    def test_mixed_numbers(self):
        """Test with mixed positive and negative numbers"""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([0, -5, 10, -2]), 10)

    def test_single_element(self):
        """Test with a single element"""
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([-5]), -5)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer())

    def test_duplicate_max(self):
        """Test with duplicate maximum values"""
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)
        self.assertEqual(max_integer([1, 2, 3, 3]), 3)

    def test_max_at_beginning(self):
        """Test with max at the beginning"""
        self.assertEqual(max_integer([5, 1, 2, 3]), 5)

    def test_max_at_middle(self):
        """Test with max in the middle"""
        self.assertEqual(max_integer([1, 5, 2, 3]), 5)

    def test_max_at_end(self):
        """Test with max at the end"""
        self.assertEqual(max_integer([1, 2, 3, 5]), 5)

    def test_all_same(self):
        """Test with all elements the same"""
        self.assertEqual(max_integer([7, 7, 7]), 7)

    def test_floats(self):
        """Test with float numbers"""
        self.assertEqual(max_integer([1.5, 2.7, 3.9, 2.1]), 3.9)

    def test_zero(self):
        """Test with zero"""
        self.assertEqual(max_integer([0, 0, 0]), 0)
        self.assertEqual(max_integer([-1, 0, 1]), 1)


if __name__ == '__main__':
    unittest.main()
