from locators import MainPageLocators
from urls import URLS
from constants import SectionTitles
from helpers.helpers import Helpers


class TestBurgerConstructorNavigation:

    def test_switch_to_buns_section(self, driver):
        """Проверка перехода к разделу булок"""
        driver.get(URLS.MAIN_PAGE)
        
        # Переходим к соусам, затем возвращаемся к булкам
        driver.find_element(*MainPageLocators.SAUCES_SECTION_BTN).click()
        driver.find_element*(MainPageLocators.BUNS_SECTION_BTN).click()
        
        # Проверяем, что секция булок активна
        assert Helpers._check_section_is_active(driver, MainPageLocators.BUNS_SECTION_BTN)
        
        buns_header = driver.find_element(*MainPageLocators.BUNS_HEADER)
        buns_section = driver.find_element(*MainPageLocators.BUNS_SECTION)
        
        assert buns_header.text == SectionTitles.BUNS
        assert buns_section.is_displayed()

    def test_switch_to_sauces_section(self, driver):
        """Проверка перехода к разделу соусов"""
        driver.get(URLS.MAIN_PAGE)
        
        driver.find_element(*MainPageLocators.SAUCES_SECTION_BTN).click()
        
        # Проверяем, что секция соусов активна
        assert Helpers._check_section_is_active(driver, MainPageLocators.SAUCES_SECTION_BTN)
        
        sauces_header = driver.find_element(*MainPageLocators.SAUCES_HEADER)
        sauces_section = driver.find_element(*MainPageLocators.SAUCES_SECTION)
        
        assert sauces_header.text == SectionTitles.SAUCES
        assert sauces_section.is_displayed()

    def test_switch_to_toppings_section(self, driver):
        """Проверка перехода к разделу начинок"""
        driver.get(URLS.MAIN_PAGE)
        
        driver.find_element(*MainPageLocators.TOPPINGS_SECTION_BTN).click()
        
        # Проверяем, что секция начинок активна
        assert Helpers._check_section_is_active(driver, MainPageLocators.TOPPINGS_SECTION_BTN)
        
        toppings_header = driver.find_element(*MainPageLocators.TOPPINGS_HEADER)
        toppings_section = driver.find_element(*MainPageLocators.TOPPINGS_SECTION)
        
        assert toppings_header.text == SectionTitles.TOPPINGS
        assert toppings_section.is_displayed()