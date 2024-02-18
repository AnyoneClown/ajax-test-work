import subprocess

from utils.logging_config import logger


def get_udid() -> str:
    udid_process = subprocess.run(["adb", 'devices', '-l'], shell=True, text=True, capture_output=True)
    udid = udid_process.stdout.split()[4]
    logger.info(f"Device UDID: {udid}")
    return udid


def android_get_desired_capabilities() -> dict:
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
