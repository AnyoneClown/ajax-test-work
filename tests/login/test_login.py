import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import TimeoutException

from framework import LoginPage


@pytest.mark.parametrize("email, password, expected_result", [
    ("invalid_email", "valid_password", False),
    ("qa.ajax.app.automation@gmail.com", "qa_automation_password", True),
])
def test_user_login(user_login_fixture: LoginPage, email: str, password: str, expected_result: bool) -> None:
    user_login_fixture.login(email, password)

    try:
        user_login_fixture.find_element((AppiumBy.ID, "com.ajaxsystems:id/hubAdd"), timeout=5)
        button_found = True
    except TimeoutException:
        user_login_fixture.click_element((AppiumBy.ID, "com.ajaxsystems:id/back"))
        button_found = False

    assert button_found == expected_result

def test_user_logout(user_login_fixture: LoginPage) -> None:
    user_login_fixture.logout()
    logo = user_login_fixture.find_element((AppiumBy.ID, "com.ajaxsystems:id/logo"))
    assert logo