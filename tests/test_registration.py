from data import UserCredentials, TestUserData
from locators import RegistrationFormLocators, AuthFormLocators
from urls import URLS
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.helpers import Helpers


class TestUserRegistration:

    def test_successful_registration(self, driver):
        """Успешная регистрация нового пользователя"""
        driver.get(URLS.REGISTRATION_PAGE)
        
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(RegistrationFormLocators.REGISTER_BUTTON)
        )
        
        Helpers._fill_registration_form(
            driver, 
            TestUserData.generate_username(),
            TestUserData.generate_email(),
            TestUserData.generate_password()
        )
        
        driver.find_element(*RegistrationFormLocators.REGISTER_BUTTON).click()
        
        login_button = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(AuthFormLocators.LOGIN_BUTTON)
        )
        
        assert driver.current_url == URLS.LOGIN_PAGE
        assert login_button.is_displayed()

    def test_registration_with_short_password(self, driver):
        """Регистрация с паролем менее 6 символов"""
        driver.get(URLS.REGISTRATION_PAGE)
        
        Helpers._fill_registration_form(
            driver,
            UserCredentials.USERNAME,
            UserCredentials.EMAIL,
            "12345"  # Слишком короткий пароль
        )
        
        driver.find_element(*RegistrationFormLocators.REGISTER_BUTTON).click()
        
        error_message = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(RegistrationFormLocators.ERROR_INVALID_PASSWORD)
        )
        
        assert error_message.text == 'Некорректный пароль'
        assert driver.current_url == URLS.REGISTRATION_PAGE

    def test_duplicate_registration_attempt(self, driver):
        """Попытка повторной регистрации существующего пользователя"""
        driver.get(URLS.REGISTRATION_PAGE)
        
        Helpers._fill_registration_form(
            driver,
            UserCredentials.USERNAME,
            UserCredentials.EMAIL,
            UserCredentials.PASSWORD
        )
        
        driver.find_element(*RegistrationFormLocators.REGISTER_BUTTON).click()
        
        error_message = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(RegistrationFormLocators.ERROR_EXISTING_USER)
        )
        
        assert error_message.text == 'Такой пользователь уже существует'
        assert driver.current_url == URLS.REGISTRATION_PAGE