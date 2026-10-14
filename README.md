
# ECommerce Automation Framework

An end-to-end web UI automation framework built using Python, Selenium WebDriver, and Pytest to test the SauceDemo e-commerce application.

## Project Features

- Login testing with valid and invalid credentials
- Data-driven testing using Pytest parametrization
- Page Object Model (POM)
- Product selection and Add to Cart validation
- Cart validation and checkout flow
- Pytest fixtures for browser setup and teardown
- Smoke and regression markers
- HTML test reports
- Failure screenshot capture
- Execution logging

## Tech Stack

- Python
- Selenium WebDriver
- Pytest
- pytest-html
- Git and GitHub

## Project Structure

```text
ECommerce_Automation/
├── pages/
│   ├── login_page.py
│   ├── product_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/
│   ├── test_login.py
│   └── test_checkout_flow.py
├── utils/
│   └── logger.py
├── reports/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/anjali-malvi/ECommerce_Automation.git
cd ECommerce_Automation
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run all tests

```bash
python -m pytest -v
```

### 6. Generate an HTML report

```bash
python -m pytest -v --html=reports/report.html --self-contained-html
```

## Test Scenarios

- Verify successful login
- Verify invalid login credentials
- Verify required-field validation
- Verify product addition to cart
- Verify cart contents
- Verify checkout completion

## Reporting

HTML reports and failure screenshots are generated locally during test execution. These files are excluded from Git tracking.

## Author

Anjali
