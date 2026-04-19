import pytest

from pages.checkboxes_page import CheckboxesPage
from pages.inputs_page import InputsPage


@pytest.mark.ui
def test_number_input_accepts_a_value(driver, base_url: str) -> None:
    inputs_page = InputsPage(driver, base_url)

    inputs_page.open()
    inputs_page.enter_number("42")

    assert inputs_page.current_value == "42"


@pytest.mark.ui
def test_checkboxes_can_be_toggled(driver, base_url: str) -> None:
    checkboxes_page = CheckboxesPage(driver, base_url)

    checkboxes_page.open()
    checkboxes_page.set_checkbox(1, True)
    checkboxes_page.set_checkbox(2, False)

    assert checkboxes_page.is_checked(1) is True
    assert checkboxes_page.is_checked(2) is False

