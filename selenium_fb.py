# Modules to be imported.
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

class facebook_session:

    FB_URL = "https://www.facebook.com"

    def __init__(self, username, password):
        self.name       = username
        self.password   = password

        # Turn off popup notification
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference("dom.webnotifications.enabled", False)

        print("Starting firefox brower ...")
        self.driver = webdriver.Firefox(firefox_profile = firefox_profile)
        self.logined = False

    def login(self):

        if self.logined == True:
            print("login: the sesssion is alreay login, do nothing")
            return True

        try:

            # Access URL
            print("login: access FaceBook site " + facebook_session.FB_URL)
            self.driver.get(facebook_session.FB_URL)

            # Facebook login.
            print("login: input username: " + self.name)
            username = self.driver.find_element_by_name("email")
            username.send_keys(self.name)

            print("login: input password: " + "*****")
            password = self.driver.find_element_by_name("pass")
            password.send_keys(self.password)

            print("login: save_screenshot login_1.png")
            self.driver.save_screenshot("login_1.png")

            login = self.driver.find_element_by_xpath("//button[text()='Đăng nhập']|//input[@value='Đăng nhập']")
            login.click()

            # Waiting for userNavigationLabel ready
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//div[@id="userNavigationLabel"]')))
            print("login: save_screenshot login_2.png")
            self.driver.save_screenshot("login_2.png")

            self.logined = True

        except Exception as e:
            print("An exception occurred: " + str(e))
            return False
        return True

    def logout(self):

        if self.logined == False:
            print("logout: the sesssion is alreay logout, do nothing")
            return False

        try:
            # Facebook logout.
            logout1 = self.driver.find_element_by_css_selector("#userNavigationLabel")
            logout1.click()

            # Waiting for logout ready
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//span[text() = "Log Out"]|//span[text()="Đăng xuất"]')))

            logout2 = self.driver.find_element_by_xpath('//span[text()="Log Out"]|//span[text()="Đăng xuất"]')

            print("login: save_screenshot logout_1.png")
            self.driver.save_screenshot("logout_1.png")

            logout2.click()

            time.sleep(2)

            print("login: save_screenshot logout_2.png")
            self.driver.save_screenshot("logout_2.png")
            self.driver.quit()

        except Exception as e:
            print("An exception occurred: " + str(e))
            return False

        return True

if __name__ == '__main__':
    fb = facebook_session("xxx", "xxx")

    if fb.login() != True:
        print("Cannot test login")
        sys.exit(1)

    if fb.logout() != True:
        print("Cannot test logout")
        sys.exit(1)

    sys.exit(0)
