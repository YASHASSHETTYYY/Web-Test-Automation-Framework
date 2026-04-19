from __future__ import annotations

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    PATH = "/login"

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH_MESSAGE = (By.ID, "flash")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a.button.secondary.radius")

    def open(self) -> None:  # type: ignore[override]
        super().open(self.PATH)

    def login(self, username: str, password: str) -> None:
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    @property
    def flash_message(self) -> str:
        raw_message = self.text_of(self.FLASH_MESSAGE)
        return raw_message.replace("×", "").strip()

    def logout_button_is_visible(self) -> bool:
        return self.is_visible(self.LOGOUT_BUTTON)

