#!/usr/bin/env python

import unittest
from datetime import date
from days import get_days


class TestGetDays(unittest.TestCase):
    """Test the get_days function."""
    
    def test_get_days_basic(self):
        """Test basic functionality with default Tue/Thu."""
        # Starting Jan 22, 2018 (a Monday), get 2 weeks of Tue/Thu
        results = get_days(2018, 1, 22, ['Tue', 'Thu'], weeks=2)
        
        # Should get: Tue Jan 23, Thu Jan 25, Tue Jan 30, Thu Feb 1
        self.assertEqual(len(results), 4)
        self.assertTrue(results[0].startswith('Tue Jan 23'))
        self.assertTrue(results[1].startswith('Thu Jan 25'))
        self.assertTrue(results[2].startswith('Tue Jan 30'))
        self.assertTrue(results[3].startswith('Thu Feb'))
    
    def test_get_days_single_weekday(self):
        """Test with a single weekday."""
        # Get 2 weeks of Mondays starting Jan 22, 2018
        results = get_days(2018, 1, 22, ['Mon'], weeks=2)
        
        # Should get 2 Mondays: Jan 22 and Jan 29
        self.assertEqual(len(results), 2)
        self.assertTrue(all('Mon' in r for r in results))
    
    def test_get_days_three_weekdays(self):
        """Test with three weekdays."""
        # Get 2 weeks of Mon/Wed/Fri starting Jan 22, 2018 (Monday)
        results = get_days(2018, 1, 22, ['Mon', 'Wed', 'Fri'], weeks=2)
        
        # Should get 6 days total (3 days × 2 weeks)
        self.assertEqual(len(results), 6)
    
    def test_get_days_weekend(self):
        """Test with weekend days."""
        # Get 2 weeks of Sat/Sun starting Jan 20, 2018 (Saturday)
        results = get_days(2018, 1, 20, ['Sat', 'Sun'], weeks=2)
        
        # Should get 4 days (2 weekends)
        self.assertEqual(len(results), 4)
        self.assertTrue('Sat' in results[0])
        self.assertTrue('Sun' in results[1])
    
    def test_get_days_starts_on_requested_day(self):
        """Test when start date is one of the requested weekdays."""
        # Jan 23, 2018 is a Tuesday, ask for Tuesdays
        results = get_days(2018, 1, 23, ['Tue'], weeks=2)
        
        # Should include the start date
        self.assertGreater(len(results), 0)
        self.assertTrue(results[0].startswith('Tue Jan 23'))
    
    def test_get_days_crossing_month_boundary(self):
        """Test that results properly cross month boundaries."""
        # Start late January, get several weeks
        results = get_days(2018, 1, 29, ['Tue', 'Thu'], weeks=3)
        
        # Should have dates in both January and February
        has_jan = any('Jan' in r for r in results)
        has_feb = any('Feb' in r for r in results)
        self.assertTrue(has_jan)
        self.assertTrue(has_feb)
    
    def test_get_days_zero_weeks(self):
        """Test with weeks=0."""
        results = get_days(2018, 1, 22, ['Tue', 'Thu'], weeks=0)
        self.assertEqual(len(results), 0)
    
    def test_get_days_one_week(self):
        """Test with exactly one week."""
        results = get_days(2018, 1, 22, ['Tue', 'Thu'], weeks=1)
        
        # Should get exactly 2 days (one Tue, one Thu in first week)
        self.assertEqual(len(results), 2)
    
    def test_get_days_end_of_year(self):
        """Test crossing year boundary."""
        # Start late December, get dates into January
        results = get_days(2018, 12, 25, ['Tue', 'Thu'], weeks=3)
        
        # Verify we get results
        self.assertGreater(len(results), 0)
    
    def test_get_days_leap_year(self):
        """Test with leap year (2020 has Feb 29)."""
        # Start Feb 24, 2020 (Monday) and go for 2 weeks
        results = get_days(2020, 2, 24, ['Sat', 'Sun'], weeks=2)
        
        # Should include Feb 29 (Saturday in 2020)
        has_feb_29 = any('Feb 29' in r for r in results)
        self.assertTrue(has_feb_29)
    
    def test_get_days_all_weekdays(self):
        """Test with all 7 weekdays."""
        results = get_days(2018, 1, 22, 
                          ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], 
                          weeks=1)
        
        # Should get 7 days for one week
        self.assertEqual(len(results), 7)
    
    def test_get_days_format(self):
        """Test that returned dates are in expected format."""
        results = get_days(2018, 1, 22, ['Tue'], weeks=1)
        
        # Each result should be a string starting with day of week
        for result in results:
            self.assertIsInstance(result, str)
            self.assertTrue(result.startswith('Tue'))


if __name__ == '__main__':
    unittest.main()
