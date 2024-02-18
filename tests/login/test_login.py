import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import TimeoutException

from framework import LoginPage
from utils.logging_config import logger


@pytest.mark.parametrize(
    "email, password, expected_result",
    [
        ("invalid_email", "valid_password", False),
        ("qa.ajax.app.automation@gmail.com", "valid_password", False),
        ("qa.ajax.app.automation@gmail.com", "qa_automation_password", True),
    ],
    ids=["Ivalid credentials", "Wrong password", "Valid credentials"]
)
def test_user_login(user_login_fixture: LoginPage, email: str, password: str, expected_result: bool) -> None:
    logger.info(f"Logging in with email: {email} and password: {password}")
    user_login_fixture.login(email, password)

    try:
        user_login_fixture.find_element((AppiumBy.ID, "com.ajaxsystems:id/hubAdd"), timeout=5)
        button_found = True
    except TimeoutException:
        logger.error("Timeout while waiting for the 'Hub Button' button")
        user_login_fixture.click_element((AppiumBy.ID, "com.ajaxsystems:id/back"))
        button_found = False

    assert button_found == expected_result


@pytest.mark.parametrize(
    "locator, exit_button, expected_element",
    [
        (
            (AppiumBy.ID, "com.ajaxsystems:id/settings"),
            (AppiumBy.ID, "com.ajaxsystems:id/back"),
            (AppiumBy.ID, "com.ajaxsystems:id/toolbarTitle"),
        ),
        (
            (AppiumBy.ID, "com.ajaxsystems:id/help"),
            (AppiumBy.ID, "com.ajaxsystems:id/back"),
            (AppiumBy.ID, "com.ajaxsystems:id/navigation"),
        ),
        (
            (AppiumBy.ID, "com.ajaxsystems:id/logs"),
            (AppiumBy.ID, "com.ajaxsystems:id/sendButton"),
            (AppiumBy.ID, "com.ajaxsystems:id/content"),
        ),
        (
            (AppiumBy.ID, "com.ajaxsystems:id/camera"),
            (AppiumBy.ID, "com.ajaxsystems:id/back"),
            (AppiumBy.ID, "com.ajaxsystems:id/toolbarTitle"),
        ),
        (
            (AppiumBy.ID, "com.ajaxsystems:id/addHub"),
            (AppiumBy.ID, "com.ajaxsystems:id/backButton"),
            (AppiumBy.ID, "com.ajaxsystems:id/title"),
        ),
    ],
    ids=["Settings", "Help", "Logs", "Camera", "Add Hub"]
)
def test_sidebar_components(user_login_fixture, locator, exit_button, expected_element):
    logger.info(
        f"Testing sidebar component with locator: {locator}, exit button: {exit_button}, expected element: {expected_element}"
    )
    user_login_fixture.click_element((AppiumBy.ID, "com.ajaxsystems:id/menuDrawer"))
    user_login_fixture.click_element(locator)
    assert user_login_fixture.find_element(expected_element)
    user_login_fixture.click_element(exit_button)


def test_user_logout(user_login_fixture: LoginPage) -> None:
    logger.info("Test logging out")
    user_login_fixture.logout()
    assert user_login_fixture.find_element((AppiumBy.ID, "com.ajaxsystems:id/logo"))
