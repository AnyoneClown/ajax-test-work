import subprocess
import time
import pytest

from appium import webdriver
from appium.options.common import AppiumOptions

from utils.android_utils import android_get_desired_capabilities
from utils.logging_config import logger


@pytest.fixture(scope='session')
def run_appium_server():
    logger.info("Starting Appium server")
    subprocess.Popen(
        ['appium', '-a', '0.0.0.0', '-p', '4723', '--allow-insecure', 'adb_shell'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True
    )
    time.sleep(5)
    logger.info("Appium server started successfully")


@pytest.fixture(scope='session')
def driver(run_appium_server):
    logger.info("Creating Appium driver session")
    driver = webdriver.Remote('http://localhost:4723/wd/hub', options=AppiumOptions().load_capabilities(android_get_desired_capabilities()))
    yield driver
