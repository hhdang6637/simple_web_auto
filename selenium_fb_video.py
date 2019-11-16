# Modules to be imported.
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

class facebook_session:

    FB_URL = "https://www.facebook.com"
    LINK_VIDEO = "https://www.facebook.com/LearnEnglishTeens.BritishCouncil/videos/1761555490566271/"
    RETURN_CURRENT_TIME = "return document.getElementsByTagName('video')[0].currentTime"
    RETURN_READY_STATE = "return document.getElementsByTagName('video')[0].readyState"
    PAUSE_VIDEO = "document.getElementsByTagName('video')[0].pause()"
    PLAY_VIDEO = "document.getElementsByTagName('video')[0].play()"

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
            self.driver.save_screenshot("login_error.png")
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
            self.driver.save_screenshot("logout_error.png")
            return False

        return True

    def waiting_video_ready(self, state):
        time_out = 0

        while int(state) != 4:
            if time_out > 20: return False
            time.sleep(1)
            time_out = time_out + 1
            state = self.driver.execute_script(self.RETURN_READY_STATE)
        return True

    def play_video(self):
        try:
            # Access URL
            print("Access FaceBook Video site " + facebook_session.LINK_VIDEO)
            self.driver.get(facebook_session.LINK_VIDEO)

            print("video: save_screenshot access_video.png")
            self.driver.save_screenshot("access_video.png")

            # Waiting for video ready
            getStateVideo = self.driver.execute_script(self.RETURN_READY_STATE)

            if facebook_session.waiting_video_ready(self, int(getStateVideo)) == True:
                isVideoStart = False
                current_time = self.driver.execute_script(self.RETURN_CURRENT_TIME)
                duration = self.driver.execute_script("return document.getElementsByTagName('video')[0].duration")

                # Waiting for video play
                while current_time < duration:
                    if int(current_time) > 1:
                        isVideoStart = True
                        break
                    current_time = self.driver.execute_script(self.RETURN_CURRENT_TIME)

                if isVideoStart:
                    self.driver.execute_script(self.PAUSE_VIDEO)
                    print("video: save_screenshot video_playing_at_the_begging.png")
                    self.driver.save_screenshot("video_playing_at_the_begging.png")

                    # Video load to the middle
                    self.driver.execute_script("document.getElementsByTagName('video')[0].currentTime = %s" %(int(duration)/2))
                    getStateVideo_at_middle = self.driver.execute_script(self.RETURN_READY_STATE)

                    if facebook_session.waiting_video_ready(self, int(getStateVideo_at_middle)) == True:
                        # self.driver.execute_script(self.PAUSE_VIDEO)
                        self.driver.execute_script(self.PLAY_VIDEO)
                        time.sleep(3)
                        print("video: save_screenshot video_playing_at_the_middle.png")
                        self.driver.save_screenshot("video_playing_at_the_middle.png")
                    else:
                        self.driver.save_screenshot("time_out_load video_to_the_middle.png")
                        return False

                    # Video load to approximate end
                    self.driver.execute_script("return document.getElementsByTagName('video')[0].currentTime = %s" %(int(duration) - 10))
                    getStateVideo_at_the_end = self.driver.execute_script(self.RETURN_READY_STATE)

                    if facebook_session.waiting_video_ready(self, int(getStateVideo_at_the_end)) == True:
                        self.driver.execute_script(self.PAUSE_VIDEO)
                        time.sleep(1)
                        print("video: save_screenshot video_playing_at_the_end.png")
                        self.driver.save_screenshot("video_playing_at_the_end.png")
                    else:
                        self.driver.save_screenshot("time_out_load video_to_the_end.png")
                        return False

                else:
                    self.driver.save_screenshot("error_video_start.png")
                    return False

            else:
                self.driver.save_screenshot("error_time_out_video_playing.png")
                return False

        except Exception as e:
            print("An exception occurred: " + str(e))
            self.driver.save_screenshot("Error play video.png")
            return False
        return True

if __name__ == '__main__':
    fb = facebook_session(os.environ["FB_USER"], os.environ["FB_PASS"])

    if fb.login() != True:
        print("Cannot test login")
        sys.exit(1)
    
    if fb.play_video() != True:
        print("Cannot test run video")
        sys.exit(1)

    if fb.logout() != True:
        print("Cannot test logout")
        sys.exit(1)

    sys.exit(0)

