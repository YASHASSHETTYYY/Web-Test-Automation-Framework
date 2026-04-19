from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage


class DropdownPage(BasePage):
    PATH = "/dropdown"

    DROPDOWN = (By.ID, "dropdown")

    def open(self) -> None:  # type: ignore[override]
        super().open(self.PATH)

    def choose_option(self, option_text: str) -> None:
        self.select_by_text(self.DROPDOWN, option_text)

    @property
    def selected_option(self) -> str:
        return self.find(self.DROPDOWN).get_attribute("value")

    @property
    def selected_option_text(self) -> str:
        return Select(self.find(self.DROPDOWN)).first_selected_option.text
