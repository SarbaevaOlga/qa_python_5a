from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, PersonalAccountLocators, RegistrationFormLocators
from urls import URLS


class Helpers:
    
    @staticmethod
    def _open_personal_account(driver):
        """Вспомогательный метод для открытия личного кабинета"""
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BTN).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(PersonalAccountLocators.LOGOUT_BUTTON)
        )

    @staticmethod
    def _verify_constructor_page_loaded(driver):
        """Вспомогательный метод для проверки загрузки конструктора"""
        buns_section = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.BUNS_SECTION)
        )
        assert driver.current_url == URLS.MAIN_PAGE
        assert buns_section.is_displayed()

    @staticmethod
    def _fill_registration_form(driver, username, email, password):
        """Вспомогательный метод для заполнения формы регистрации"""
        driver.find_element(*RegistrationFormLocators.NAME_INPUT).send_keys(username)
        driver.find_element(*RegistrationFormLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationFormLocators.PASSWORD_INPUT).send_keys(password)

    @staticmethod
    def _check_section_is_active(driver, section_button_locator):
        """Проверяет, что секция активна (имеет класс 'tab_tab_type_current')"""
        section_element = driver.find_element(*section_button_locator)
        class_attribute = section_element.get_attribute("class")
        return "tab_tab_type_current" in class_attribute