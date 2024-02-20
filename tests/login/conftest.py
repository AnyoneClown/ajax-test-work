import pytest

from framework.login_page import LoginPage


@pytest.fixture(scope="function")
def user_login_fixture(driver):
    yield LoginPage(driver)


@pytest.fixture(scope="module")
def login_once(driver):
    LoginPage(driver).login("qa.ajax.app.automation@gmail.com", "qa_automation_password")
