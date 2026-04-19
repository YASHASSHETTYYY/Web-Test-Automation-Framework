# Web Test Automation Framework

This project is a small Selenium + Pytest automation framework built with a Page Object Model structure. It uses the public site `https://the-internet.herokuapp.com` for UI coverage and `https://jsonplaceholder.typicode.com` for a lightweight API smoke test.

## What is included

- Selenium UI tests for login, form controls, and dropdowns
- Page Object Model structure for reusable page actions
- `pytest-html` reporting with self-contained HTML output
- GitHub Actions workflow that runs on every push
- A Postman collection for the API covered by the test suite

## Project structure

```text
.
|-- .github/workflows/tests.yml
|-- pages/
|   |-- __init__.py
|   |-- base_page.py
|   |-- checkboxes_page.py
|   |-- dropdown_page.py
|   |-- inputs_page.py
|   `-- login_page.py
|-- postman/
|   `-- jsonplaceholder_collection.json
|-- tests/
|   |-- api/test_jsonplaceholder_api.py
|   |-- ui/test_dropdown.py
|   |-- ui/test_forms.py
|   |-- ui/test_login.py
|   `-- conftest.py
|-- pytest.ini
`-- requirements.txt
```

## Setup

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run tests

Run the full suite:

```powershell
pytest
```

Run only UI tests:

```powershell
pytest -m ui
```

Run only API tests:

```powershell
pytest -m api
```

Run with a visible browser window:

```powershell
pytest -m ui --headed
```

Run with Microsoft Edge instead of Chrome:

```powershell
pytest -m ui --browser=edge
```

## Reporting

The HTML report is generated automatically at:

```text
reports/report.html
```

If a UI test fails, a screenshot is saved under:

```text
reports/screenshots/
```

## Test targets

UI site:

- `https://the-internet.herokuapp.com/login`
- `https://the-internet.herokuapp.com/inputs`
- `https://the-internet.herokuapp.com/checkboxes`
- `https://the-internet.herokuapp.com/dropdown`

API:

- `https://jsonplaceholder.typicode.com/posts/1`

## Postman

The collection lives at:

```text
postman/jsonplaceholder_collection.json
```

