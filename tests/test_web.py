

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage


def test_navigation_to_search_engine(browser):
    phrase = 'panda'

    search_page = DuckDuckGoSearchPage(browser)
    search_page.load()
    search_page.search(phrase)

    result_page = DuckDuckGoResultPage(browser)
    assert result_page.link_div_count() > 0
    assert result_page.phrase_result_count(phrase) > 0
    assert result_page.search_input_value() == phrase


def test_search(browser):
    phrase = 'garmin'

    search_page = DuckDuckGoSearchPage(browser)
    search_page.load()
    search_page.search(phrase)
