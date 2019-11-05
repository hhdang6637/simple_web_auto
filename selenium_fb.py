# Modules to be imported.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

# Login account
email = "Your Email"
passwd = "Your Password"
URL = "https://www.facebook.com"

# Turn off popup notification
firefox_profile=webdriver.FirefoxProfile()
firefox_profile.set_preference("dom.webnotifications.enabled", False)

# Browser : Firefox.
driver = webdriver.Firefox(firefox_profile = firefox_profile)

# Access URL
driver.get(URL)

# Facebook login.
username = driver.find_element_by_name("email")
username.send_keys(email)

password = driver.find_element_by_name("pass")
password.send_keys(passwd)

login = driver.find_element_by_xpath("//button[text()='Đăng nhập']|//input[@value='Đăng nhập']")
login.click()

# Waiting for userNavigationLabel ready
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//div[@id="userNavigationLabel"]')))

# Facebook logout.
logout1=driver.find_element_by_css_selector("#userNavigationLabel")
logout1.click()

# Waiting for logout ready
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//span[text()="Log Out"]|//span[text()="Đăng xuất"]')))

logout2=driver.find_element_by_xpath('//span[text()="Log Out"]|//span[text()="Đăng xuất"]')
logout2.click()

time.sleep(2)
driver.quit()