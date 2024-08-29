# Web Application Testing Framework(python)

This framework is designed for automating UI tests of web applications using Python, Selenium WebDriver, and pytest.

## Project Structure

```
python-web-testing/
│
├── tests/
│   ├── test_elements_page.py
│   └── ...
│
├── pages/
│   ├── elements_page.py
│   └── ...
│
├── utils/
│   ├── test_base.py
│   ├── excel_util.py
│   └── test_util.py
│
├── conftest.py
├── requirements.txt
└── README.md
```

## Setup

1. Ensure you have Python 3.7+ installed.
2. Clone this repository:
   
3. Create a virtual environment:
   
4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Configuration

- Update `utils/test_base.py` to configure your WebDriver settings.
- Place your test data Excel files in a `test_data/` directory.

## Running Tests

To run all tests:
```
pytest tests/
```

To generate an HTML report:
```
pytest tests/ --html=report.html
```

## Key Components

1. **test_base.py**: Base class for all tests, handling WebDriver setup and teardown.
2. **conftest.py**: Contains pytest fixtures and hooks for test execution.
3. **excel_util.py**: Utility for reading test data from Excel files.
4. **test_util.py**: Contains common test utility functions.
5. **pages/*.py**: Page Object Model classes for different pages of the web application.
6. **tests/*.py**: Test case files containing actual test methods.

## Writing Tests

1. Create a new test file in the `tests/` directory.
2. Import the necessary Page Object and utility classes.
3. Write test methods using pytest conventions.
4. Use data-driven testing with `@pytest.mark.parametrize` when needed.


## Continuous Integration

This framework can be integrated with CI/CD tools like Jenkins, GitLab CI, or GitHub Actions. Configure the CI to:

1. Set up a Python environment
2. Install dependencies
3. Run tests
4. Generate and publish test reports
