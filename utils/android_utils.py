import subprocess

from utils.logging_config import logger


def get_udid():
    try:
        udid = subprocess.run(["adb", 'devices', '-l'], shell=True, text=True, capture_output=True)
        logger.info(f"Device UDID: {udid}")
        return udid.stdout.split()[0]
    except Exception as e:
        logger.error("Failed to get device UDID", exc_info=True)
        return "adb-414e7250-OZJrqe._adb-tls-connect._tcp"


def android_get_desired_capabilities():
    return {
        "autoGrantPermissions": True,
        "automationName": "uiautomator2",
        "newCommandTimeout": 500,
        "noSign": True,
        "platformName": "Android",
        "platformVersion": "11",
        "resetKeyboard": True,
        "systemPort": 8301,
        "takesScreenshot": True,
        "udid": get_udid(),
        "appPackage": "com.ajaxsystems",
        "appActivity": "com.ajaxsystems.ui.activity.LauncherActivity",
    }
