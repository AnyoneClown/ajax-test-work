import pytest
from appium.webdriver.common.appiumby import AppiumBy

from framework import LoginPage
from utils.logging_config import logger


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
    ids=["Settings", "Help", "Logs", "Camera", "Add Hub"],
)
def test_sidebar_components(
    login_once: LoginPage, user_login_fixture: LoginPage, locator: tuple, exit_button: tuple, expected_element: tuple
) -> None:
    logger.info(
        f"Testing sidebar component with locator: {locator}, exit button: {exit_button}, expected element: {expected_element}"
    )
    user_login_fixture.click_element((AppiumBy.ID, "com.ajaxsystems:id/menuDrawer"))
    user_login_fixture.click_element(locator)
    assert user_login_fixture.find_element(expected_element)
    user_login_fixture.click_element(exit_button)
