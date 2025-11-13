import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AuthFormLocators
from urls import URLS
from data import UserCredentials


@pytest.fixture
def driver():
    """Фикстура для инициализации драйвера"""
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()


@pytest.fixture
def authenticated_driver(driver):
    """Фикстура для предварительной авторизации пользователя"""
    driver.get(URLS.MAIN_PAGE)
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BTN).click()
    
    driver.find_element(*AuthFormLocators.EMAIL_INPUT).send_keys(UserCredentials.EMAIL)
    driver.find_element(*AuthFormLocators.PASSWORD_INPUT).send_keys(UserCredentials.PASSWORD)
    driver.find_element(*AuthFormLocators.LOGIN_BUTTON).click()
    
    # Ожидаем загрузки главной страницы после авторизации
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BTN)
    )
    
    return driver