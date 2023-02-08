import time
import platform

from selenium.webdriver.common.by import By
import chromedriver_autoinstaller

import chrome_tools

if __name__ == "__main__":

    chromedriver_autoinstaller.install()
    chrome_tools.open_chrome_profile()
    while True:
        if platform.system() == "Darwin":
            break
        if chrome_tools.is_port_in_use() == True:
            break

    browser = chrome_tools.get_webdriver()
    browser.get('https://www.google.com')

    try:
        browser.find_element(By.XPATH, '/html/head/title')
    except:
        pass

    print("Selenium is ready")