#!/usr/bin/env python

import unittest
from days import _grouper


class TestGrouper(unittest.TestCase):
    """Test the _grouper utility function."""
    
    def test_grouper_even_division(self):
        """Test grouping when items divide evenly."""
        data = [1, 2, 3, 4, 5, 6]
        result = list(_grouper(data, 2))
        expected = [(1, 2), (3, 4), (5, 6)]
        self.assertEqual(result, expected)
    
    def test_grouper_uneven_division(self):
        """Test grouping when items don't divide evenly."""
        data = [1, 2, 3, 4, 5]
        result = list(_grouper(data, 2))
        expected = [(1, 2), (3, 4), (5, None)]
        self.assertEqual(result, expected)
    
    def test_grouper_single_item_groups(self):
        """Test grouping with n=1."""
        data = [1, 2, 3]
        result = list(_grouper(data, 1))
        expected = [(1,), (2,), (3,)]
        self.assertEqual(result, expected)
    
    def test_grouper_larger_groups(self):
        """Test grouping with larger group size."""
        data = [1, 2, 3, 4, 5, 6, 7]
        result = list(_grouper(data, 3))
        expected = [(1, 2, 3), (4, 5, 6), (7, None, None)]
        self.assertEqual(result, expected)
    
    def test_grouper_custom_fillvalue(self):
        """Test grouping with custom fill value."""
        data = [1, 2, 3, 4, 5]
        result = list(_grouper(data, 2, fillvalue='X'))
        expected = [(1, 2), (3, 4), (5, 'X')]
        self.assertEqual(result, expected)
    
    def test_grouper_empty_list(self):
        """Test grouping an empty list."""
        data = []
        result = list(_grouper(data, 2))
        expected = []
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
