# Tests for days

This directory contains a comprehensive test suite for the `days` module using Python's built-in `unittest` framework.

## Running Tests

### Run all tests with verbose output:
```bash
python3 -m unittest discover tests -v
```

### Run all tests (simple):
```bash
python3 -m unittest discover tests
```

### Run a specific test file:
```bash
python3 -m unittest tests.test_get_days
```

### Run a specific test class:
```bash
python3 -m unittest tests.test_get_days.TestGetDays
```

### Run a specific test method:
```bash
python3 -m unittest tests.test_get_days.TestGetDays.test_get_days_basic
```

### Use the test runner script:
```bash
python3 tests/run_tests.py
```

## Test Organization

- **`test_grouper.py`** - Tests for the `_grouper()` utility function
  - Even and uneven division
  - Custom fill values
  - Edge cases (empty lists, single items)

- **`test_get_days.py`** - Tests for the `get_days()` core function
  - Basic functionality with various weekday combinations
  - Month and year boundary crossing
  - Leap year handling
  - Output format validation

- **`test_main.py`** - Tests for the `main()` output formatting function
  - Default vs grouped output
  - Different weekday configurations
  - Output format validation

- **`test_cli.py`** - Tests for CLI argument parsing and integration
  - All command-line flags and options
  - Argument validation
  - Flag aliases (--weekdays vs --on)
  - Date override behavior

## Test Coverage

The test suite covers:
- ✅ All public functions
- ✅ Edge cases and boundary conditions
- ✅ Error handling
- ✅ CLI argument parsing
- ✅ Output formatting
- ✅ Date calculations including leap years

## Dependencies

The test suite uses **only** Python standard library modules:
- `unittest` - Test framework
- `unittest.mock` - For patching sys.argv and datetime
- `io.StringIO` - For capturing stdout
- `sys`, `os`, `datetime` - Standard utilities

No external testing frameworks or dependencies are required.
