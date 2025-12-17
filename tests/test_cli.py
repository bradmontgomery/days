#!/usr/bin/env python

import unittest
import sys
from io import StringIO
from unittest.mock import patch
from datetime import datetime
from days import cli


class TestCLI(unittest.TestCase):
    """Test the CLI argument parsing and integration."""
    
    def setUp(self):
        """Capture stdout for testing."""
        self.held_output = StringIO()
        self.original_stdout = sys.stdout
        sys.stdout = self.held_output
    
    def tearDown(self):
        """Restore stdout."""
        sys.stdout = self.original_stdout
    
    def test_cli_with_year_month_dom(self):
        """Test CLI with -y, -m, -d flags."""
        test_args = ['days.py', '-y', '2018', '-m', '1', '-d', '22', '-n', '1']
        with patch.object(sys, 'argv', test_args):
            cli()
        
        output = self.held_output.getvalue()
        self.assertGreater(len(output), 0)
    
    def test_cli_with_start_date(self):
        """Test CLI with --start-date flag."""
        test_args = ['days.py', '--start-date', '2018-01-22', '-n', '1']
        with patch.object(sys, 'argv', test_args):
            cli()
        
        output = self.held_output.getvalue()
        self.assertGreater(len(output), 0)
    
    def test_cli_with_weekdays_flag(self):
        """Test CLI with -w/--weekdays flag."""
        test_args = ['days.py', '-y', '2018', '-m', '1', '-d', '22', 
                     '-w', 'Mon', 'Wed', '-n', '1']
        with patch.object(sys, 'argv', test_args):
            cli()
        
        output = self.held_output.getvalue()
        self.assertGreater(len(output), 0)
    
    def test_cli_with_on_flag(self):
        """Test CLI with --on alias for weekdays."""
        test_args = ['days.py', '-y', '2018', '-m', '1', '-d', '22',
                     '--on', 'Tue', 'Thu', '-n', '1']
        with patch.object(sys, 'argv', test_args):
            cli()
        
        output = self.held_output.getvalue()
        self.assertGreater(len(output), 0)
    
    def test_cli_with_group_flag(self):
        """Test CLI with -g/--group flag."""
        test_args = ['days.py', '-y', '2018', '-m', '1', '-d', '22', 
                     '-n', '2', '-g']
        with patch.object(sys, 'argv', test_args):
            cli()
        
        output = self.held_output.getvalue()
        # Should contain separator lines
        self.assertIn('----------', output)
    
    def test_cli_with_num_weeks(self):
        """Test CLI with -n/--num-weeks flag."""
        test_args = ['days.py', '-y', '2018', '-m', '1', '-d', '22',
                     '--num-weeks', '3']
        with patch.object(sys, 'argv', test_args):
            cli()
        
        output = self.held_output.getvalue()
        lines = [l for l in output.strip().split('\n') if l and not l.startswith('-')]
        
        # With 3 weeks of Tue/Thu, should get 6 lines
        self.assertEqual(len(lines), 6)
    
    def test_cli_start_date_overrides_ymd(self):
        """Test that --start-date overrides -y, -m, -d."""
        # Provide conflicting dates
        test_args = ['days.py', 
                     '-y', '2020', '-m', '6', '-d', '15',  # One date
                     '--start-date', '2018-01-22',  # Different date
                     '-n', '1']
        with patch.object(sys, 'argv', test_args):
            cli()
        
        output = self.held_output.getvalue()
        # Should use 2018-01-22 from --start-date (dates will be in Jan)
        self.assertIn('Jan', output)
    
    def test_cli_invalid_start_date_format(self):
        """Test that invalid --start-date format raises error."""
        test_args = ['days.py', '--start-date', 'invalid-date']
        
        with patch.object(sys, 'argv', test_args):
            with self.assertRaises(SystemExit):
                # argparse.error() calls sys.exit()
                cli()
    
    def test_cli_default_values(self):
        """Test CLI with no arguments uses defaults."""
        test_args = ['days.py']
        
        # Mock datetime.now() to have predictable defaults
        mock_now = datetime(2018, 1, 22, 10, 0, 0)
        with patch('days.datetime') as mock_datetime:
            mock_datetime.now.return_value = mock_now
            mock_datetime.strptime = datetime.strptime
            
            with patch.object(sys, 'argv', test_args):
                cli()
        
        output = self.held_output.getvalue()
        # Should produce some output with defaults
        self.assertGreater(len(output), 0)
    
    def test_cli_dom_flag(self):
        """Test that --dom flag works."""
        test_args = ['days.py', '-y', '2018', '-m', '1', '--dom', '22', '-n', '1']
        with patch.object(sys, 'argv', test_args):
            cli()
        
        output = self.held_output.getvalue()
        self.assertGreater(len(output), 0)
    
    def test_cli_multiple_weekdays(self):
        """Test with multiple weekdays specified."""
        test_args = ['days.py', '-y', '2018', '-m', '1', '-d', '22',
                     '--weekdays', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri',
                     '-n', '1']
        with patch.object(sys, 'argv', test_args):
            cli()
        
        output = self.held_output.getvalue()
        lines = [l for l in output.strip().split('\n') if l and not l.startswith('-')]
        
        # Should get 5 weekdays in one week
        self.assertEqual(len(lines), 5)


if __name__ == '__main__':
    unittest.main()
