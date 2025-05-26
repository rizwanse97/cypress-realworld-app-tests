from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "http://localhost:3000/signin"

class LoginPage:
    def __init__(self, driver, timeout: int = 5):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    username_loc = (By.ID,  "username")
    password_loc = (By.ID,  "password")
    signin_btn_loc = (By.CSS_SELECTOR, '[data-test="signin-submit"]')
    signup_link_loc = (By.CSS_SELECTOR, '[data-test="signup"]')
    user_help_loc = (By.ID, "username-helper-text")
    error_msg_loc = (By.CSS_SELECTOR, '[data-test="signin-error"]')
    remember_chk_loc = (By.CSS_SELECTOR, 'input[name="remember"]')
    my_account_lbl_loc = (By.XPATH, "//*[contains(text(), 'My Account')]")

   
    def load(self):
        self.driver.get(BASE_URL)

    def set_username(self, value: str | None):
        element = self.driver.find_element(*self.username_loc)
        element.clear()
        if value is not None:
            element.send_keys(value)

    def set_password(self, value: str | None):
        element = self.driver.find_element(*self.password_loc)
        element.clear()
        if value is not None:
            element.send_keys(value)

    def click_signin(self):
        self.driver.find_element(*self.signin_btn_loc).click()

    def click_signup(self):
        self.wait.until(EC.element_to_be_clickable(self.signup_link_loc)).click()

    def toggle_remember_me(self, desired_state: bool):
        chk = self.driver.find_element(*self.remember_chk_loc)
        if chk.is_selected() != desired_state:
            chk.click()
    
    @property
    def username_error_text(self) -> str:
        return self.wait.until(EC.visibility_of_element_located(self.user_help_loc)).text

    @property
    def login_error_text(self) -> str:
        return self.wait.until(EC.visibility_of_element_located(self.error_msg_loc)).text

    @property
    def is_signin_enabled(self) -> bool:
        return self.driver.find_element(*self.signin_btn_loc).is_enabled()

    @property
    def username_value(self) -> str:
        return self.driver.find_element(*self.username_loc).get_attribute("value")

    @property
    def password_value(self) -> str:
        return self.driver.find_element(*self.password_loc).get_attribute("value")

    def wait_for_dashboard(self):
        self.wait.until(EC.visibility_of_element_located(self.my_account_lbl_loc))
