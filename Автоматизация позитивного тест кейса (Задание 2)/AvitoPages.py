from BaseApp import BasePage
from selenium.webdriver.common.by import By


class AvitoSearchLocators:
    LOCATOR_AVITO_FAVORITE_BUTTON = (By.CLASS_NAME, 'desktop-p6xjn6')


class FavoriteButtonPress(BasePage):

    def click_button(self):
        return self.find_element(AvitoSearchLocators.LOCATOR_AVITO_FAVORITE_BUTTON, time=2).click()

