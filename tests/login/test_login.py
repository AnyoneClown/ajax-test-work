import time

import pytest
from appium.webdriver.common.appiumby import AppiumBy

from framework import LoginPage
from utils.logging_config import logger


@pytest.mark.parametrize(
    "email, password, expected_result",
    [
        ("invalid_email", "valid_password", False),
        ("qa.ajax.app.automation@gmail.com", "valid_password", False),
        ("qa.ajax.app.automation@gmail.com", "qa_automation_password", True),
    ],
    ids=["Invalid credentials", "Wrong password", "Valid credentials"],
)
def test_user_login(user_login_fixture: LoginPage, email: str, password: str, expected_result: bool) -> None:
    logger.info(f"Logging in with email: {email} and password: {password}")
    user_login_fixture.login(email, password)

    if expected_result:
        result = user_login_fixture.is_element_present((AppiumBy.ID, "com.ajaxsystems:id/hubAdd"), timeout=5)
    else:
        result = user_login_fixture.is_element_present((AppiumBy.ID, "com.ajaxsystems:id/back"))
        time.sleep(2)
        user_login_fixture.click_element((AppiumBy.ID, "com.ajaxsystems:id/back"))

    assert result


def test_user_logout(user_login_fixture: LoginPage) -> None:
    logger.info("Test logging out")
    user_login_fixture.logout()
    assert user_login_fixture.find_element((AppiumBy.ID, "com.ajaxsystems:id/logo"))
