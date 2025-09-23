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

#function for switching to frame
def switch_to_frame(driver,iframe_xpath):
    iframe=driver.find_element(By.XPATH,iframe_xpath)
    driver.switch_to.frame(iframe)

# Get text from an element inside a frame (nested frame)
def get_text_from_element(driver, text_xpath):
    element=driver.find_element(By.XPATH,text_xpath)
    return element.text

def main():
    parent_frame_xpath = "//frame[@name='frame-top']"
    child_frame_xpath = "//frame[@name='frame-middle']"
    text_xpath = "//div[@id='content']"
    url= "https://the-internet.herokuapp.com/nested_frames"

    driver=initialize_driver()

    open_url(driver,url)

    WebDriverWait(driver,5).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,parent_frame_xpath)))
    switch_to_frame(driver, child_frame_xpath)

    text=get_text_from_element(driver, text_xpath)
    print("the text inside the child frame is: ",text)

    #go back from the child frame
    driver.switch_to.parent_frame()
    print("switched back to the parent frame")

    #go back from the parent frame
    driver.switch_to.default_content()
    print("switched back from all the frames")

    driver.quit()

if __name__ == "__main__":
    main()
