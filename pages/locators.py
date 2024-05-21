


from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    EMAIL = (By.CSS_SELECTOR, '#id_login-username')
    PASSWORD = (By.CSS_SELECTOR, '#id_login-password')
    EMAIL_REGISTER = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD_REGISTER = (By.CSS_SELECTOR, '#id_registration-password1')

