import os
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import selenium.webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from bs4 import BeautifulSoup



def get_chromedriver():
    """Download chromedriver if not found."""
    if not os.path.isfile('chromedriver'):
        print('Downloading chromedriver...')
        if os.name == "posix" :
            r = requests.get('https://chromedriver.storage.googleapis.com/100.0.4896.20/chromedriver_linux64.zip')
            with open('chromedriver.zip', 'wb') as f:
                f.write(r.content)
            os.system('unzip chromedriver.zip')
            os.remove('chromedriver.zip')
            os.chmod('chromedriver', 0o755)
        elif os.name == "nt" :
            r = requests.get('https://chromedriver.storage.googleapis.com/100.0.4896.20/chromedriver_win32.zip')
            with open('chromedriver.zip', 'wb') as f:
                f.write(r.content)
            os.system('unzip chromedriver.zip')
            os.remove('chromedriver.zip')
            os.chmod('chromedriver', 0o755)
        else :
            raise OSError("Unsupported OS")
    return os.path.abspath('chromedriver')


def get_geckodriver():
    """Download geckodriver if not found."""
    if not os.path.isfile('geckodriver'):
        print('Downloading geckodriver...')
        if os.name == "posix" :
            r = requests.get('https://github.com/mozilla/geckodriver/releases/download/v0.34.0/geckodriver-v0.34.0-linux64.tar.gz')
            with open('geckodriver.tar.gz', 'wb') as f:
                f.write(r.content)
            os.system('tar -xvzf geckodriver.tar.gz')
            os.remove('geckodriver.tar.gz')
            os.chmod('geckodriver', 0o755)
            return os.path.abspath('geckodriver')
        elif os.name == "nt" :
            r = requests.get('https://github.com/mozilla/geckodriver/releases/download/v0.34.0/geckodriver-v0.34.0-win-aarch64.zip')
            with open('geckodriver.zip', 'wb') as f:
                f.write(r.content)
            os.system('unzip geckodriver.zip')
            os.remove('geckodriver.zip')
            os.chmod('geckodriver', 0o755)
            return os.path.abspath('geckodriver')
        else :
            raise OSError("Unsupported OS")
    return os.path.abspath('geckodriver')

DRIVER = None

def get_driver(type=None, headless=True) :
    global DRIVER
    if DRIVER is None:
        if type is None :
            raise RuntimeError("No driver type specified")
        elif type == "chrome" :
            chrome_options = Options()
            if headless :
                chrome_options.add_argument("--headless")
            chrome_options.add_argument("--incognito")
            service = ChromeService(executable_path=get_chromedriver(), options=chrome_options)
            DRIVER = webdriver.Chrome(service=service)
            DRIVER.__setattr__("find_element_by_css_selector", lambda selector : find_element_by_css_selector(DRIVER, selector))
        elif type == "firefox" :
            firefox_options = Options()
            if headless :
                firefox_options.add_argument("--headless")
            firefox_options.add_argument("--incognito")
            service = FirefoxService(executable_path=get_geckodriver())
            DRIVER = webdriver.Firefox(service=service, options=firefox_options)
            DRIVER.__setattr__("find_element_by_css_selector", lambda selector : find_element_by_css_selector(DRIVER, selector))
    return DRIVER


def browseto(url) :
    get_driver().get(url)

def find_element_by_css_selector(driver, selector):
    element = driver.find_element(By.CSS_SELECTOR, selector)
    return element

def clickon(selector) :
    get_driver().find_element_by_css_selector(selector).click()

def typein(selector,text) :
    get_driver().find_element_by_css_selector(selector).send_keys(text)

def checkfor(selector) :
    return get_driver().find_element_by_css_selector(selector).is_displayed()

DEFAULTS = {
    "browseto" : browseto,
    "clickon" : clickon,
    "typein" : typein,
    "checkfor" : checkfor
}
