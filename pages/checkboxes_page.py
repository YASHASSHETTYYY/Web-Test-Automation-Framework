from __future__ import annotations

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckboxesPage(BasePage):
    PATH = "/checkboxes"

    CHECKBOXES = (By.CSS_SELECTOR, "#checkboxes input")

    def open(self) -> None:  # type: ignore[override]
        super().open(self.PATH)

    def _checkbox(self, index: int):
        self.wait.until(lambda driver: len(driver.find_elements(*self.CHECKBOXES)) >= index)
        checkboxes = self.driver.find_elements(*self.CHECKBOXES)
        return checkboxes[index - 1]

    def set_checkbox(self, index: int, checked: bool) -> None:
        checkbox = self._checkbox(index)
        if checkbox.is_selected() != checked:
            checkbox.click()

    def is_checked(self, index: int) -> bool:
        return self._checkbox(index).is_selected()
