#!/usr/bin/env python

import unittest
import sys
from io import StringIO
from argparse import Namespace
from days import main


class TestMain(unittest.TestCase):
    """Test the main function that handles output formatting."""
    
    def setUp(self):
        """Capture stdout for testing."""
        self.held_output = StringIO()
        self.original_stdout = sys.stdout
        sys.stdout = self.held_output
    
    def tearDown(self):
        """Restore stdout."""
        sys.stdout = self.original_stdout
    
    def test_main_default_output(self):
        """Test main with default output (no grouping)."""
        args = Namespace(
            year=2018,
            month=1,
            day=22,
            dows=['Tue', 'Thu'],
            weeks=2,
            chunk=False
        )
        main(args)
        
        output = self.held_output.getvalue()
        lines = output.strip().split('\n')
        
        # Should have 4 lines (2 weeks × 2 days)
        self.assertEqual(len(lines), 4)
        
        # Each line should be 10 characters (the [:10] slice)
        for line in lines:
            self.assertEqual(len(line), 10)
    
    def test_main_grouped_output(self):
        """Test main with grouped output."""
        args = Namespace(
            year=2018,
            month=1,
            day=22,
            dows=['Tue', 'Thu'],
            weeks=2,
            chunk=True
        )
        main(args)
        
        output = self.held_output.getvalue()
        lines = output.strip().split('\n')
        
        # Should have separator lines
        self.assertTrue(any('----------' in line for line in lines))
        
        # Count separator lines (should be 2 for 2 weeks)
        separator_count = sum(1 for line in lines if '----------' in line)
        self.assertEqual(separator_count, 2)
    
    def test_main_default_dows(self):
        """Test that None dows defaults to Tue/Thu."""
        args = Namespace(
            year=2018,
            month=1,
            day=22,
            dows=None,  # Should default to ['Tue', 'Thu']
            weeks=1,
            chunk=False
        )
        main(args)
        
        output = self.held_output.getvalue()
        lines = output.strip().split('\n')
        
        # Should get 2 days (Tue and Thu)
        self.assertEqual(len(lines), 2)
    
    def test_main_single_weekday(self):
        """Test with a single weekday."""
        args = Namespace(
            year=2018,
            month=1,
            day=22,
            dows=['Mon'],
            weeks=2,
            chunk=False
        )
        main(args)
        
        output = self.held_output.getvalue()
        lines = output.strip().split('\n')
        
        # Should get 2 Mondays
        self.assertEqual(len(lines), 2)
    
    def test_main_grouped_with_three_days(self):
        """Test grouping with three weekdays."""
        args = Namespace(
            year=2018,
            month=1,
            day=22,
            dows=['Mon', 'Wed', 'Fri'],
            weeks=2,
            chunk=True
        )
        main(args)
        
        output = self.held_output.getvalue()
        
        # Should have separators
        self.assertIn('----------', output)
    
    def test_main_output_format(self):
        """Test that output is in correct format (10 chars)."""
        args = Namespace(
            year=2018,
            month=1,
            day=22,
            dows=['Tue'],
            weeks=1,
            chunk=False
        )
        main(args)
        
        output = self.held_output.getvalue()
        lines = [l for l in output.strip().split('\n') if l and not l.startswith('-')]
        
        # Each date line should be exactly 10 characters
        for line in lines:
            self.assertEqual(len(line), 10)


if __name__ == '__main__':
    unittest.main()
