import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


#function for intializing the driver
def initialize_driver():
    service=Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver

#funtion for URL
def open_url(driver,url):
    driver.get(url)

#function for switch to frame using Xpath
def switch_to_frame(driver, iframe_xpath):
    iframe=driver.find_element(By.XPATH,iframe_xpath)
    driver.switch_to.frame(iframe)

#function for entering text into input
def enter_text(driver, text_xpath, text):
    input_field=driver.find_element(By.XPATH,text_xpath)
    input_field.send_keys(text)

def main():
    parent_frame_xpath = "//iframe[@id='firstFr']"
    first_name_input_xpath = "//input[@name='fname']"
    last_name_input_xpath = "//input[@name='lname']"
    child_frame_xpath = "//iframe[@src='innerframe']"
    email_input_xpath = "//input[@name='email']"
    url=  "https://letcode.in/frame"

    driver=initialize_driver()

    open_url(driver, url)

    wait=WebDriverWait(driver, 5)

    # switch to parent frame
    switch_to_frame(driver, parent_frame_xpath)
    time.sleep(2)

    enter_text(driver, first_name_input_xpath, "jhon")
    time.sleep(2)
    enter_text(driver, last_name_input_xpath, "Doe")
    time.sleep(2)

    print("first and last name has been entered!")

    #switch to nested frame
    switch_to_frame(driver, child_frame_xpath)
    enter_text(driver, email_input_xpath,"jhon1122@gmail.com")

    print("email has been entered!")

    time.sleep(2)

    #switch to parent frame
    driver.switch_to.parent_frame()
    print("switched back to the parent frame")

    #switched back from all the frames
    driver.switch_to.default_content()
    print("switched back from all the frames")

    time.sleep(2)
    driver.quit()

if __name__ == "__main__":
    main()
