# WebTest Framework  

A **scalable test automation framework** built with **Python, Selenium, Pytest, and Page Object Model (POM)**.  

This framework is designed to provide:  

- Maintainable test scripts  
- Reusable page objects and utility functions  
- Excel-driven test data support  
- Logging and screenshot capture on failure  
- HTML/Allure reporting integration  

---

## 📂 Project Structure  

``` bash

webtest-automation-framework/
├── base/                # Base classes (BasePage with common Selenium actions)
├── configfiles/         # Config files (YAML, Python parser)
├── logs/                # Execution logs
├── pages/               # Page Object Model classes
├── reports/             # Test execution reports (pytest-html / allure)
├── screenshots/         # Screenshots captured on test failures
├── testcases/           # Test case files
├── testdata/            # Excel or other test data
├── utilities/           # Reusable utilities (logger, excel reader, functions)
├── conftest.py          # Pytest fixtures & hooks
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
├── LICENSE              # License file

````

---

## ⚙️ Setup  

### 1. Clone Repository  

```bash
git clone https://github.com/<your-username>/webtest-framework.git
cd webtest-framework
````

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running Tests

### Run all tests

```bash
pytest
```

### Run tests with HTML report

```bash
pytest --html=reports/report.html --self-contained-html
```

### Run tests with Allure report (if enabled)

```bash
pytest --alluredir=reports/allure-results
allure serve reports/allure-results
```

---

## 🧩 Key Features

- **Page Object Model (POM)** → Keeps test logic separate from UI element locators.
- **Config-driven** → Centralized config (`config.yaml`) for browser, URL, and timeouts.
- **Test Data Support** → Read test data from Excel sheets for parametrized tests.
- **Logging** → Structured logs stored in `logs/` with `utils.py`.
- **Screenshots** → Captures screenshots on test failures and attaches them to reports.
- **Reports** → Supports `pytest-html` and `allure-pytest`.

---

## 📌 Example Test Flow

1. Test loads browser fixture from `conftest.py`.
2. Navigates to application URL (from `config.yaml`).
3. Uses `LoginPage` class (from `pages/`) to perform login.
4. Validates expected result using assertions in test case.
5. On failure → logs details + saves screenshot + attaches to HTML/Allure report.

---

## 📜 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---
