from appium.webdriver.common.appiumby import AppiumBy

from .page import Page


class LoginPage(Page):
    email_field = (AppiumBy.ID, "com.ajaxsystems:id/authLoginEmail")
    password_field = (AppiumBy.ID, "com.ajaxsystems:id/authLoginPassword")
    login_button = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.Button")
    confirm_button = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView[2]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.Button")

    def login(self, email: str, password: str) -> None:
        """Login to the application with provided credentials"""

        self.click_element(self.login_button)
        self.clean_field_value(self.email_field)
        self.insert_value(self.email_field, email)
        self.insert_value(self.password_field, password)
        self.click_element(self.confirm_button)
