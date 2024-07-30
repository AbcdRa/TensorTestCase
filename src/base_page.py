from selenium.webdriver.remote.webdriver import WebDriver
from pathlib import Path

class BasePage(object):
    def __init__(self, driver:WebDriver):
        self.driver = driver
        self.WEBDRIVER_TIMEOUT = 10
        self.WEBDRIVER_ACTION_PAUSE = 0.5


    def is_download_finished(self, temp_folder):
        firefox_temp_file = sorted(Path(temp_folder).glob('*.part'))
        chrome_temp_file = sorted(Path(temp_folder).glob('*.crdownload'))
        downloaded_files = sorted(Path(temp_folder).glob('*.*'))
        if (len(firefox_temp_file) == 0) and \
        (len(chrome_temp_file) == 0) and \
        (len(downloaded_files) >= 1):
            return True
        else:
            return False

