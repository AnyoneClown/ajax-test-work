import subprocess

from utils.logging_config import logger


def get_udid():
    try:
        udid = subprocess.check_output(["adb", "get-serialno"]).decode("utf-8").strip()
        logger.info(f"Device UDID: {udid}")
        return udid
    except Exception as e:
        logger.error("Failed to get device UDID", exc_info=True)
        return None


def android_get_desired_capabilities():
    udid = get_udid()

    if not udid:
        udid = "adb-414e7250-OZJrqe._adb-tls-connect._tcp"

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
        "udid": udid,
        "appPackage": "com.ajaxsystems",
        "appActivity": "com.ajaxsystems.ui.activity.LauncherActivity",
    }
