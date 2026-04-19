from __future__ import annotations

import os
from pathlib import Path
from typing import Generator

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

ROOT_DIR = Path(__file__).resolve().parents[1]
REPORTS_DIR = ROOT_DIR / "reports"
SCREENSHOTS_DIR = REPORTS_DIR / "screenshots"
SELENIUM_CACHE_DIR = ROOT_DIR / ".selenium"
CHROME_BINARY_PATHS = (
    Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
    Path(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"),
)
EDGE_BINARY_PATHS = (
    Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
    Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
)


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--base-url",
        action="store",
        default=os.getenv("BASE_URL", "https://the-internet.herokuapp.com"),
        help="Base URL for UI tests.",
    )
    parser.addoption(
        "--api-base-url",
        action="store",
        default=os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com"),
        help="Base URL for API tests.",
    )
    parser.addoption(
        "--browser",
        action="store",
        default=os.getenv("BROWSER", "chrome").lower(),
        choices=("chrome", "edge"),
        help="Browser used for UI tests.",
    )
    parser.addoption(
        "--headed",
        action="store_true",
        default=False,
        help="Run UI tests with a visible browser window.",
    )


def pytest_configure(config: pytest.Config) -> None:
    REPORTS_DIR.mkdir(exist_ok=True)
    SCREENSHOTS_DIR.mkdir(exist_ok=True)
    SELENIUM_CACHE_DIR.mkdir(exist_ok=True)


def _first_existing_path(paths: tuple[Path, ...]) -> str | None:
    for path in paths:
        if path.exists():
            return str(path)
    return None


@pytest.fixture(scope="session")
def base_url(pytestconfig: pytest.Config) -> str:
    return pytestconfig.getoption("base_url")


@pytest.fixture(scope="session")
def api_base_url(pytestconfig: pytest.Config) -> str:
    return pytestconfig.getoption("api_base_url")


@pytest.fixture
def driver(request: pytest.FixtureRequest) -> Generator[webdriver.Remote, None, None]:
    browser = request.config.getoption("browser")
    headless = not request.config.getoption("headed") and os.getenv("HEADLESS", "true").lower() == "true"
    os.environ.setdefault("SE_CACHE_PATH", str(SELENIUM_CACHE_DIR))

    if browser == "chrome":
        options = ChromeOptions()
        chrome_binary = _first_existing_path(CHROME_BINARY_PATHS)
        if chrome_binary:
            options.binary_location = chrome_binary
        options.add_argument("--window-size=1440,1080")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        if headless:
            options.add_argument("--headless=new")
        web_driver = webdriver.Chrome(options=options)
    else:
        options = EdgeOptions()
        options.use_chromium = True
        edge_binary = _first_existing_path(EDGE_BINARY_PATHS)
        if edge_binary:
            options.binary_location = edge_binary
        options.add_argument("--window-size=1440,1080")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        if headless:
            options.add_argument("--headless=new")
        web_driver = webdriver.Edge(options=options)

    web_driver.implicitly_wait(2)
    yield web_driver

    report = getattr(request.node, "rep_call", None)
    if report and report.failed:
        screenshot_name = request.node.nodeid.replace("\\", "_").replace("/", "_").replace("::", "__")
        screenshot_path = SCREENSHOTS_DIR / f"{screenshot_name}.png"
        web_driver.save_screenshot(str(screenshot_path))

        pytest_html = request.config.pluginmanager.getplugin("html")
        if pytest_html:
            extras = getattr(report, "extras", [])
            extras.append(pytest_html.extras.image(str(screenshot_path)))
            report.extras = extras

    web_driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item, call: pytest.CallInfo[None]):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)
