from base.base_driver import init_driver
from page.display_page import DisplayPage


class TestDisplay:
    def setup(self):
        self.driver = init_driver()

        self.display_page = DisplayPage(self.driver)

    def test_display(self):
        self.display_page.click_display_btn()

        self.display_page.click_search_btn()

        self.display_page.input_search_edit_text_btn('text')

        self.display_page.click_back_btn()