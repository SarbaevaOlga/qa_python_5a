from locators import MainPageLocators
from urls import URLS
from helpers.helpers import Helpers


class TestBurgerConstructorNavigation:

    def test_switch_to_buns_section(self, driver):
        """Проверка перехода к разделу булок"""
        driver.get(URLS.MAIN_PAGE)
        
        driver.find_element(*MainPageLocators.SAUCES_SECTION_BTN).click()
        driver.find_element*(MainPageLocators.BUNS_SECTION_BTN).click()
        
        assert Helpers._check_section_is_active(driver, MainPageLocators.BUNS_SECTION_BTN)

    def test_switch_to_sauces_section(self, driver):
        """Проверка перехода к разделу соусов"""
        driver.get(URLS.MAIN_PAGE)
        
        driver.find_element(*MainPageLocators.SAUCES_SECTION_BTN).click()
        
        assert Helpers._check_section_is_active(driver, MainPageLocators.SAUCES_SECTION_BTN)
        
    def test_switch_to_toppings_section(self, driver):
        """Проверка перехода к разделу начинок"""
        driver.get(URLS.MAIN_PAGE)
        
        driver.find_element(*MainPageLocators.TOPPINGS_SECTION_BTN).click()
        
        assert Helpers._check_section_is_active(driver, MainPageLocators.TOPPINGS_SECTION_BTN)