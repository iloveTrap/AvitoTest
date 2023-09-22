from AvitoPages import FavoriteButtonPress


def test_avito_selected(browser):
    avito_page = FavoriteButtonPress(browser)
    avito_page.go_to_site()
    avito_page.click_button()
