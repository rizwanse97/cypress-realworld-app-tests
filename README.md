
# Login Test Automation Report

## Frameworks and Tools Used

- **Programming Language**: Python  
- **Automation Framework**: Selenium WebDriver  
- **Test Runner**: Pytest  
- **Design Pattern**: Page Object Model (POM)  

---

## Objective

The goal was to automate the login functionality of the **Real World App** using **Selenium with Python and Pytest**, utilizing the **Page Object Model** design pattern.  
The automation covers end-to-end validation of login logic, UI feedback, field behaviors, and session cookie handling through a structured and scalable approach.

---

## Automated Test Cases Summary

| Test Case ID   | Description                                                                                   | Status |
|----------------|-----------------------------------------------------------------------------------------------|--------|
| TC_Login_01    | Login with valid Username and Password                                                        | Pass |
| TC_Login_02    | Login with invalid Username and invalid Password                                              | Pass |
| TC_Login_03    | Login with invalid Username and valid Password                                                | Pass |
| TC_Login_04    | Login with valid Username and invalid Password                                                | Pass |
| TC_Login_05    | Leave both fields blank and try to sign in                                                    | Pass |
| TC_Login_06    | Leave Username blank, enter valid Password and try to sign in                                 | Pass |
| TC_Login_07    | Enter valid Username, leave the Password blank and try to sign in                             | Pass |
| TC_Login_08    | Verify Sign Up link navigation                                                                | Fail |
| TC_Login_09    | Verify Password Field is Masking                                                              | Pass |
| TC_Login_10    | Verify Long Input Strings for username and password fields                                    | Fail |
| TC_Login_11    | Verify if "Remember Me" checkbox is checked the persistent cookie has expiry                  | Pass |
| TC_Login_12    | Verify if "Remember Me" is unchecked, the session cookie should have no expiry                | Pass |

---

## Explanation of Failed Test Cases

### TC_Login_08: Sign Up Link Navigation
- **Issue**: The link requires two clicks to navigate, which may indicate a delayed DOM update or JavaScript handler lag.

### TC_Login_10: Long Input Strings
- **Issue**: Username/password fields allow input beyond standard limits (username > 50, password > 128).

---

## Project Structure

```
project-root/
│
├── pages/
│   └── login_page.py   
├── tests/
│   └── test_login.py     
└── requirements.txt    
```

---

## Instructions for Running the Tests

1. In `login_page.py`, update the `BASE_URL` to match your local or test environment.
2. Create a test user in the application.
3. In `test_login.py`, set the `VALID_USERNAME` and `VALID_PASSWORD` variables with the credentials of the test user.
