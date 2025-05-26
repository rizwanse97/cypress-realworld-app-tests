import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage

VALID_USERNAME = "rizwan"
VALID_PASSWORD  = "test1234"

@pytest.fixture(scope="function")
def driver():
    opts = Options()
    service = Service()
    drv = webdriver.Chrome(service=service, options=opts)
    yield drv
    drv.quit()

@pytest.fixture(scope="function")
def login_page(driver):
    page = LoginPage(driver)
    page.load()
    return page

#TC_Login_01: Login with valid Username and valid Password
def test_valid_login(login_page):
    login_page.set_username(VALID_USERNAME)
    login_page.set_password(VALID_PASSWORD)
    login_page.click_signin()
    login_page.wait_for_dashboard()

#TC_Login_02: Login with invalid Username and invalid Password
def test_invalid_username_and_password(login_page):
    login_page.set_username("rizwan89")
    login_page.set_password("test899")
    login_page.click_signin()
    assert "username or password is invalid" in login_page.login_error_text.lower()

#TC_Login_03:Login with invalid Username and valid Password.
def test_invalid_username_valid_password(login_page):
    login_page.set_username("rizwan89")
    login_page.set_password(VALID_PASSWORD)
    login_page.click_signin()
    assert "username or password is invalid" in login_page.login_error_text.lower()

#TC_Login_04: Login with valid Username and invalid Password.
def test_valid_username_invalid_password(login_page):
    login_page.set_username(VALID_USERNAME)
    login_page.set_password("test899")
    login_page.click_signin()
    assert "username or password is invalid" in login_page.login_error_text.lower()

#TC_Login_05: Leave both fields blank and try to sign in.
def test_blank_username_and_password(login_page):
    login_page.set_username("")
    login_page.set_password("")
    assert "username is required" in login_page.username_error_text.lower()
    assert not login_page.is_signin_enabled

#TC_Login_06: Leave Username blank, enter valid Password and try to sign in.
def test_blank_username(login_page):
    login_page.set_username("")
    login_page.set_password(VALID_PASSWORD)
    assert "username is required" in login_page.username_error_text.lower()
    assert not login_page.is_signin_enabled

#TC_Login_07: Enter valid Username, leave Password blank and try to sign in.
def test_blank_password(login_page):
    login_page.set_username(VALID_USERNAME)
    login_page.set_password("")
    assert not login_page.is_signin_enabled

#TC_Login_08: Verify Sign up link navigation
def test_signup_link_navigation(login_page):
    login_page.click_signup()
    assert "/signup" in login_page.driver.current_url

#TC_Login_09: Verify Password Field is masking
def test_password_field_masking(login_page):
    input_type = login_page.driver.find_element(*LoginPage.password_loc).get_attribute("type")
    assert input_type == "password"

#TC_Login_10: Verify Long Input Strings
def test_long_input_client_side_restriction(login_page):
    login_page.set_username("x" * 500)
    login_page.set_password("y" * 500)
    assert len(login_page.username_value) <= 50
    assert len(login_page.password_value) <= 128

#TC_Login_11: Verify if "Remember Me" Checkbox is checked the Persistent Cookie has Expiry
def test_remember_me_checked_sets_cookie_expiry(login_page):
    login_page.set_username(VALID_USERNAME)
    login_page.set_password(VALID_PASSWORD)
    login_page.toggle_remember_me(True)
    login_page.click_signin()
    time.sleep(2)
    cookies = login_page.driver.get_cookies()
    sid = next((c for c in cookies if c["name"] == "connect.sid"), None)
    assert sid and "expiry" in sid and sid["expiry"] > time.time()

#TC_Login_12: Verify if "Remember Me" Unchecked the Session Cookie should have no Expiry
def test_remember_me_unchecked_sets_session_cookie(login_page):
    login_page.set_username(VALID_USERNAME)
    login_page.set_password(VALID_PASSWORD)
    login_page.toggle_remember_me(False)
    login_page.click_signin()
    time.sleep(2)
    cookies = login_page.driver.get_cookies()
    sid = next((c for c in cookies if c["name"] == "connect.sid"), None)
    assert sid and "expiry" not in sid

