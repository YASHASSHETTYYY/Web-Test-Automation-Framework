from __future__ import annotations

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class InputsPage(BasePage):
    PATH = "/inputs"

    NUMBER_INPUT = (By.TAG_NAME, "input")

    def open(self) -> None:  # type: ignore[override]
        super().open(self.PATH)

    def enter_number(self, value: str) -> None:
        element = self.find(self.NUMBER_INPUT)
        element.clear()
        element.send_keys(value)

    @property
    def current_value(self) -> str:
        return self.find(self.NUMBER_INPUT).get_attribute("value")

