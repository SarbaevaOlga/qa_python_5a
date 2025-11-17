from data import UserCredentials
from locators import MainPageLocators, AuthFormLocators, RegistrationFormLocators, PasswordRecoveryLocators
from urls import URLS
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestUserAuthentication:

    def test_login_via_main_page_button(self, driver):
        """Авторизация через кнопку 'Войти в аккаунт' на главной странице"""
        driver.get(URLS.MAIN_PAGE)
        driver.find_element(*MainPageLocators.LOGIN_ACCOUNT_BTN).click()
        
        self._perform_login(driver)
        self._verify_successful_login(driver)

    def test_login_via_personal_account_button(self, driver):
        """Авторизация через кнопку 'Личный кабинет'"""
        driver.get(URLS.MAIN_PAGE)
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BTN).click()
        
        self._perform_login(driver)
        self._verify_successful_login(driver)

    def test_login_from_registration_page(self, driver):
        """Авторизация со страницы регистрации"""
        driver.get(URLS.REGISTRATION_PAGE)
        driver.find_element(*RegistrationFormLocators.LOGIN_LINK).click()
        
        self._perform_login(driver)
        self._verify_successful_login(driver)

    def test_login_from_password_recovery_page(self, driver):
        """Авторизация со страницы восстановления пароля"""
        driver.get(URLS.PASSWORD_RECOVERY_PAGE)
        driver.find_element(*PasswordRecoveryLocators.LOGIN_LINK).click()
        
        self._perform_login(driver)
        self._verify_successful_login(driver)

    def _perform_login(self, driver):
        """Вспомогательный метод для выполнения авторизации"""
        email_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(AuthFormLocators.EMAIL_INPUT)
        )
        email_field.send_keys(UserCredentials.EMAIL)
        
        driver.find_element(*AuthFormLocators.PASSWORD_INPUT).send_keys(UserCredentials.PASSWORD)
        driver.find_element(*AuthFormLocators.LOGIN_BUTTON).click()

    def _verify_successful_login(self, driver):
        """Вспомогательный метод для проверки успешной авторизации"""
        order_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BTN)
        )
        
        assert driver.current_url == URLS.MAIN_PAGE
        assert order_button.text == 'Оформить заказ'