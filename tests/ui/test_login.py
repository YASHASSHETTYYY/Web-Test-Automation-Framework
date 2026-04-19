import pytest

from pages.login_page import LoginPage


@pytest.mark.ui
def test_user_can_log_in_with_valid_credentials(driver, base_url: str) -> None:
    login_page = LoginPage(driver, base_url)

    login_page.open()
    login_page.login("tomsmith", "SuperSecretPassword!")

    assert login_page.current_path == "/secure"
    assert login_page.logout_button_is_visible()
    assert "You logged into a secure area!" in login_page.flash_message

