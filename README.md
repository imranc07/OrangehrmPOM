# OrangehrmPOM
Website Link: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

## Test Objective
Launching OrangeHRM demo website and testing start automation, login functionality, click_pim functionality, click_add functionality, add_employee functionality and shutdown using pytest framework with a page object model POM Pattern. 

## Table of Contents
+ [Features]()
+ [Tech Stack]()
+ [Running Tests]()
+ [Project Structure]()

## Features
Automated Login Tests: Verifies user login functionality, including positive and negative scenarios.
Add Employee Tests: Ensures proper addition on new employee.

## Tech Stack
* Programming Language: Python
* Test Framework: pytest
* Automation Tool: Selenium WebDriver
* Reporting: pytest-html
* Browser Compatibility: Chrome, Firefox, and optionally, Edge

## Running Tests
To execute tests, use the following commands:

1. Run All Tests:
```
pytest
```
3. Generate HTML Report:
```
pytest --html=Reports/test_report.html
```
4. Headless Browser Execution:
   You can set up tests to run in headless mode directly in your test script.

## Project Structure
```
OrangeHRM/
├── tests/                     # All test cases
│   ├── test_start.py          # Start test
│   ├── test_login.py          # Login test
│   ├── test_click_pim.py      # CLick PIM button  tests
│   ├── test_click_add.py      # Click add button test
│   ├── test_add_employee.py   # and and save new employee test
│   ├── test_shutdown.py       # Browser shutdown test
├── pages/                     # Page Object Models for each page
│   ├── OrangeHRM.py
└── README.md                  # Project documentation
```
