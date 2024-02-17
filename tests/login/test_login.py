import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from framework import LoginPage


@pytest.mark.parametrize("username, password, expected_result", [
    ("qa.ajax.app.automation@gmail.com", "qa_automation_password", True),
    ("invalid_username", "valid_password", False),
])
def test_user_login(user_login_fixture: LoginPage, email: str, password: str, expected_result: bool) -> None:
    user_login_fixture.login(email, password)

    try:
        user_login_fixture.wait_for_element(By.ID, "com.ajaxsystems:id/hubAdd")
        button_found = True
    except TimeoutException:
        button_found = False

    assert button_found == expected_result
