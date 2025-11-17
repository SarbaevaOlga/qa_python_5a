from locators import MainPageLocators, PersonalAccountLocators, AuthFormLocators
from urls import URLS
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.helpers import Helpers


class TestPersonalAccountFunctionality:

    def test_navigate_to_personal_account_from_main_page(self, authenticated_driver):
        """Переход в личный кабинет с главной страницы"""
        driver = authenticated_driver
        
        account_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BTN)
        )
        account_button.click()
        
        logout_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(PersonalAccountLocators.LOGOUT_BUTTON)
        )
        save_button = driver.find_element(*PersonalAccountLocators.SAVE_BUTTON)
        
        assert driver.current_url == URLS.PROFILE_PAGE
        assert save_button.is_displayed()

    def test_navigate_from_account_to_constructor_via_button(self, authenticated_driver):
        """Переход из личного кабинета в конструктор через кнопку"""
        driver = authenticated_driver
        Helpers._open_personal_account(driver)
        
        driver.find_element(*PersonalAccountLocators.CONSTRUCTOR_BTN).click()
        
        Helpers._verify_constructor_page_loaded(driver)

    def test_navigate_from_account_to_constructor_via_logo(self, authenticated_driver):
        """Переход из личного кабинета в конструктор через логотип"""
        driver = authenticated_driver
        Helpers._open_personal_account(driver)
        
        driver.find_element(*PersonalAccountLocators.LOGO_BTN).click()
        
        Helpers._verify_constructor_page_loaded(driver)

    def test_logout_from_personal_account(self, authenticated_driver):
        """Выход из личного кабинета"""
        driver = authenticated_driver
        Helpers._open_personal_account(driver)
        
        driver.find_element(*PersonalAccountLocators.LOGOUT_BUTTON).click()
        
        login_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(AuthFormLocators.LOGIN_BUTTON)
        )
        
        assert driver.current_url == URLS.LOGIN_PAGE
        assert login_button.is_displayed()