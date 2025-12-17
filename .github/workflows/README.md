# GitHub Actions Workflows

This directory contains CI/CD workflows for the `days` project.

## Workflows

### 1. Tests (`test.yml`)
Runs the test suite on all supported Python versions using standard Python.

**Triggers:**
- Pull requests to `main`
- Pushes to `main`

**Matrix:**
- Python 3.12, 3.13, 3.14

**Steps:**
- Checkout code
- Set up Python
- Run all unittest tests
- Test CLI help command
- Test CLI execution

### 2. Test with uv (`test-uv.yml`)
Runs the test suite using the `uv` package manager to ensure compatibility.

**Triggers:**
- Pull requests to `main`
- Pushes to `main`

**Matrix:**
- Python 3.12, 3.13, 3.14

**Steps:**
- Checkout code
- Install uv
- Set up Python via uv
- Sync project dependencies
- Run tests via uv
- Test CLI commands via uv with various options

### 3. Code Quality (`quality.yml`)
Performs code quality checks and validation.

**Triggers:**
- Pull requests to `main`
- Pushes to `main`

**Checks:**
- Python syntax validation for main module
- Python syntax validation for all test files
- Verify only stdlib imports are used (no external dependencies)
- Verify minimum test count (30+ tests)

## Status Badges

Add these to your README.md to show workflow status:

```markdown
![Tests](https://github.com/YOUR_USERNAME/days/workflows/Tests/badge.svg)
![Test with uv](https://github.com/YOUR_USERNAME/days/workflows/Test%20with%20uv/badge.svg)
![Code Quality](https://github.com/YOUR_USERNAME/days/workflows/Code%20Quality/badge.svg)
```

## Local Testing

Before pushing, you can run the same checks locally:

```bash
# Run tests
python3 -m unittest discover tests -v

# Check syntax
python3 -m py_compile days.py
for f in tests/test_*.py; do python3 -m py_compile "$f"; done

# Verify stdlib-only imports
grep -r "^import\|^from" days.py tests/*.py | \
  grep -v -E "(argparse|calendar|datetime|itertools|unittest|sys|io|os)" | \
  grep -v "from days import" | \
  grep -v "from unittest.mock import"
```

## Requirements

All workflows use only:
- Standard Python (3.12, 3.13, 3.14)
- Python standard library modules
- uv package manager (for uv-specific workflow)

No external dependencies are required to run the project or tests.
