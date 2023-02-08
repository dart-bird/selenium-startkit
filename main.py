import chrome_tools
import time

from selenium.webdriver.common.by import By
import chromedriver_autoinstaller

if __name__ == "__main__":
    chromedriver_autoinstaller.install()
    chrome_tools.open_chrome_profile()
    while True:
        if chrome_tools.is_port_in_use() == True:
            break
    browser = chrome_tools.get_webdriver()

    browser.get('https://www.google.com')

    try:
        browser.find_element(By.XPATH, '/html/head/title')
    except:
        pass

    print("Selenium is ready")