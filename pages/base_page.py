from __future__ import annotations

from typing import Tuple
from urllib.parse import urlparse

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

Locator = Tuple[str, str]


class BasePage:
    def __init__(self, driver: WebDriver, base_url: str) -> None:
        self.driver = driver
        self.base_url = base_url.rstrip("/")
        self.wait = WebDriverWait(driver, 10)

    def open(self, path: str) -> None:
        self.driver.get(f"{self.base_url}{path}")

    def find(self, locator: Locator) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator: Locator) -> None:
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator: Locator, value: str) -> None:
        element = self.find(locator)
        element.clear()
        element.send_keys(value)

    def text_of(self, locator: Locator) -> str:
        return self.find(locator).text.strip()

    def select_by_text(self, locator: Locator, value: str) -> None:
        Select(self.find(locator)).select_by_visible_text(value)

    def is_visible(self, locator: Locator) -> bool:
        try:
            self.find(locator)
        except Exception:
            return False
        return True

    @property
    def current_path(self) -> str:
        return urlparse(self.driver.current_url).path

