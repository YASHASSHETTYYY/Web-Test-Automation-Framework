import pytest

from pages.dropdown_page import DropdownPage


@pytest.mark.ui
def test_dropdown_selection_is_saved(driver, base_url: str) -> None:
    dropdown_page = DropdownPage(driver, base_url)

    dropdown_page.open()
    dropdown_page.choose_option("Option 2")

    assert dropdown_page.selected_option == "2"
    assert dropdown_page.selected_option_text == "Option 2"

