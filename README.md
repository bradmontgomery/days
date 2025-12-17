days
====

[![Python Version](https://img.shields.io/badge/python-3.12%20%7C%203.13%20%7C%203.14-blue)](https://www.python.org)
[![Project Version](https://img.shields.io/badge/version-0.2.0-green)](https://github.com/bradmontgomery/days)
[![Tests](https://github.com/bradmontgomery/days/workflows/Tests/badge.svg)](https://github.com/bradmontgomery/days/actions)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE.txt)
[![Last Commit](https://img.shields.io/github/last-commit/bradmontgomery/days)](https://github.com/bradmontgomery/days/commits)

Print some days in a list.

A simple command-line tool for generating lists of specific weekdays over a given number of weeks. Perfect for planning class schedules, recurring meetings, or any activity that happens on specific days of the week.

> 🌞 **[View the Beautiful Documentation Website →](https://bradmontgomery.github.io/days/)**

## Quick Start

### Run instantly with uvx (no installation required)

```bash
# Run directly from GitHub
uvx --from git+https://github.com/bradmontgomery/days days -n 4

# With options
uvx --from git+https://github.com/bradmontgomery/days days --start-date 2025-01-15 --on Mon Wed Fri -n 3
```

## Installation

### Using uvx (recommended for one-off use)

No installation needed! Just use `uvx --from git+https://github.com/bradmontgomery/days days` followed by your options.

### Using uv (recommended for regular use)

```bash
# Clone the repository
git clone https://github.com/bradmontgomery/days.git
cd days

# Install with uv
uv sync

# Run the tool
uv run days
```

### Using standard Python

```bash
# Clone the repository
git clone https://github.com/bradmontgomery/days.git
cd days

# Run directly (Python 3.12+)
python days.py
```

## Requirements

- Python 3.12, 3.13, or 3.14
- No external dependencies (uses only Python standard library)

## Usage

```
usage: Print a list of days over a given number of weeks. [-h] [--start-date START_DATE] [-y YEAR] [-m MONTH] [-d DAY]
                                                          [-n WEEKS] [-w [WEEKDAY ...]] [-g]

options:
  -h, --help            show this help message and exit
  --start-date START_DATE
                        Start date in YYYY-MM-DD format (overrides -y, -m, -d if provided)
  -y, --year YEAR       Starting year (default: current year)
  -m, --month MONTH     Starting month (default: current month)
  -d, --dom DAY         Day of month to start (default: current day)
  -n, --num-weeks WEEKS
                        Number of weeks to print (default: 14)
  -w, --weekdays, --on [WEEKDAY ...]
                        Weekdays to print (e.g., Tue Thu) (default: Tue Thu)
  -g, --group           Group output by weeks
```

## Examples

**Note:** In all examples below, you can replace `uv run days` with:
- `uvx --from git+https://github.com/bradmontgomery/days days` (no installation)
- `python days.py` (if you cloned the repo)

The default is to print Tuesdays and Thursdays for 14 weeks, starting on the current day:

```bash
$ uv run days
# or with uvx (no installation)
$ uvx --from git+https://github.com/bradmontgomery/days days
# or directly
$ python days.py
```

Example output (if run on Jan 22, 2025):
```
Tue Jan 23
Thu Jan 25
Tue Jan 30
Thu Feb  1
Tue Feb  6
Thu Feb  8
...
```

### Specify a start date

Use `--start-date` for convenience:

```bash
$ uv run days --start-date 2025-01-15 -n 4
# or with uvx
$ uvx --from git+https://github.com/bradmontgomery/days days --start-date 2025-01-15 -n 4
```

Output:
```
Thu Jan 16
Tue Jan 21
Thu Jan 23
Tue Jan 28
Thu Jan 30
Tue Feb  4
Thu Feb  6
```

Or use individual year/month/day flags:

```bash
$ uv run days -y 2025 -m 1 --dom 15 -n 4
```

### Choose specific weekdays

Print Mondays, Wednesdays, and Fridays for 3 weeks:

```bash
$ uv run days --weekdays Mon Wed Fri -n 3
# or use the --on alias
$ uv run days --on Mon Wed Fri -n 3
```

### Group output by weeks

Print Fri, Sat, Sun for three weeks with grouping:

```bash
$ uv run days --on Fri Sat Sun -n 3 --group
Fri Jan 26
Sat Jan 27
Sun Jan 28
----------
Fri Feb  2
Sat Feb  3
Sun Feb  4
----------
Fri Feb  9
Sat Feb 10
Sun Feb 11
----------
```

### More examples

```bash
# Just Mondays for 8 weeks
$ uv run days --on Mon -n 8

# All weekdays (Mon-Fri) for 2 weeks
$ uv run days --weekdays Mon Tue Wed Thu Fri -n 2

# Weekend days starting from a specific date
$ uv run days --start-date 2025-06-01 --on Sat Sun -n 4

# Using uvx for quick one-off commands (no installation needed)
$ uvx --from git+https://github.com/bradmontgomery/days days --on Tue Thu -n 6 --group
```

## Development

### Running Tests

The project includes a comprehensive test suite using Python's `unittest`:

```bash
# Run all tests
python -m unittest discover tests -v

# Or use the test runner
python tests/run_tests.py

# With uv
uv run python -m unittest discover tests -v
```

### Project Structure

```
days/
├── days.py              # Main application
├── pyproject.toml       # Project configuration (uv)
├── tests/               # Test suite (35+ tests)
│   ├── test_grouper.py
│   ├── test_get_days.py
│   ├── test_main.py
│   └── test_cli.py
└── .github/workflows/   # CI/CD pipelines
    ├── test.yml         # Standard Python tests
    ├── test-uv.yml      # uv integration tests
    └── quality.yml      # Code quality checks
```

### Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run the tests: `python -m unittest discover tests -v`
5. Submit a pull request

All pull requests are automatically tested on Python 3.12, 3.13, and 3.14.

## Features

- 📅 Generate lists of specific weekdays over multiple weeks
- 🎯 Simple, intuitive command-line interface
- 📦 Zero external dependencies (stdlib only)
- 🐍 Supports Python 3.12, 3.13, and 3.14
- ✅ Comprehensive test coverage (35+ tests)
- 🔄 Managed with modern `uv` package manager
- ⚡ Run instantly with `uvx` (no installation required)
- 🚀 CI/CD with GitHub Actions

## Why?

I sometimes teach a class and find it handy to have a list of dates. I also haphazardly put this together over several months without ever thinking about looking at any other tools `¯\_(ツ)_/¯`.

## License

See [LICENSE.txt](LICENSE.txt) for details.
