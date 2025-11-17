from selenium.webdriver.common.by import By


class PageLocators:
    """Общие локаторы для всех страниц"""
    CONSTRUCTOR_BTN = (By.XPATH, "//p[contains(text(), 'Конструктор')]")
    ORDER_FEED_BTN = (By.XPATH, "//p[contains(text(), 'Лента Заказов')]")
    LOGO_BTN = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")
    PERSONAL_ACCOUNT_BTN = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")


class MainPageLocators(PageLocators):
    """Локаторы главной страницы"""
    MAIN_CONTAINER = (By.XPATH, "//main[contains(@class, 'App_componentContainer')]")
    LOGIN_ACCOUNT_BTN = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
    PLACE_ORDER_BTN = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    
    # Кнопки переключения категорий
    BUNS_SECTION_BTN = (By.XPATH, "//span[text()='Булки']/parent::div")
    SAUCES_SECTION_BTN = (By.XPATH, "//span[text()='Соусы']/parent::div")
    TOPPINGS_SECTION_BTN = (By.XPATH, "//span[text()='Начинки']/parent::div")
    
    # Секции ингредиентов
    BUNS_SECTION = (By.XPATH, "//h2[text()='Булки']/following-sibling::ul")
    SAUCES_SECTION = (By.XPATH, "//h2[text()='Соусы']/following-sibling::ul")
    TOPPINGS_SECTION = (By.XPATH, "//h2[text()='Начинки']/following-sibling::ul")
    
    # Заголовки секций
    BUNS_HEADER = (By.XPATH, "//h2[text()='Булки']")
    SAUCES_HEADER = (By.XPATH, "//h2[text()='Соусы']")
    TOPPINGS_HEADER = (By.XPATH, "//h2[text()='Начинки']")


class AuthFormLocators(PageLocators):
    """Локаторы формы авторизации"""
    AUTH_FORM = (By.XPATH, "//div[contains(@class, 'Auth_login')]")
    EMAIL_INPUT = (By.XPATH, "//input[@name='name' and @type='text']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль' and @type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    REGISTER_LINK = (By.XPATH, "//a[contains(text(), 'Зарегистрироваться')]")
    RECOVER_PASSWORD_LINK = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]")


class RegistrationFormLocators(PageLocators):
    """Локаторы формы регистрации"""
    NAME_INPUT = (By.XPATH, "(//input[@name='name'])[1]")
    EMAIL_INPUT = (By.XPATH, "(//input[@name='name'])[2]")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")
    LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]")
    ERROR_EXISTING_USER = (By.XPATH, "//p[contains(text(), 'Такой пользователь уже существует')]")
    ERROR_INVALID_PASSWORD = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")


class PasswordRecoveryLocators(PageLocators):
    """Локаторы восстановления пароля"""
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    RECOVER_BUTTON = (By.XPATH, "//button[contains(text(), 'Восстановить')]")
    LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]")


class PersonalAccountLocators(PageLocators):
    """Локаторы личного кабинета"""
    PROFILE_SECTION = (By.XPATH, "//div[contains(@class, 'Account_account')]")
    PROFILE_TAB = (By.XPATH, "//a[contains(text(), 'Профиль')]")
    ORDER_HISTORY_TAB = (By.XPATH, "//a[contains(text(), 'История заказов')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")
    SAVE_BUTTON = (By.XPATH, "//button[contains(text(), 'Сохранить')]")
    CANCEL_BUTTON = (By.XPATH, "//button[contains(text(), 'Отмена')]")