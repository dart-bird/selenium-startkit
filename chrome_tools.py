import os
import platform
import subprocess
import sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

main_directory = os.path.join(sys.path[0])
main_directory += '/data'

def is_port_in_use(port=8989) -> bool:
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

def open_chrome_profile(port=8989):
    if is_port_in_use(port) == False:
        if platform.system() == "Windows":
            subprocess.Popen(
            [
                "start",
                "chrome",
                "--remote-debugging-port={}".format(port),
                "--user-data-dir=" + main_directory + "/chrome_profile",
            ],
            shell=True,
            )

def get_webdriver(headless=False, port=8989) -> webdriver.Chrome:
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
    opt = Options()
    if headless == True: opt.add_argument("--headless")
    opt.add_argument(f'user-agent={user_agent}')
    if platform.system() == "Windows":
        opt.add_experimental_option("debuggerAddress", "localhost:{}".format(port))
    else:
        opt.add_argument('user-data-dir={}/chrome_profile'.format(main_directory))
        
    driver = webdriver.Chrome(options=opt)
    return driver