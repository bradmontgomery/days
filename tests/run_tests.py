#!/usr/bin/env python
"""
Test runner for the days project.
Run all tests with: python -m unittest discover tests
Or run this file directly: python tests/run_tests.py
"""

import unittest
import sys
import os

# Add parent directory to path so we can import days module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

if __name__ == '__main__':
    # Discover and run all tests in the tests directory
    loader = unittest.TestLoader()
    start_dir = os.path.dirname(os.path.abspath(__file__))
    suite = loader.discover(start_dir, pattern='test_*.py')
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Exit with non-zero status if tests failed
    sys.exit(not result.wasSuccessful())
