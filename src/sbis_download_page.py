from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_page import BasePage
import re


class SBISDownloadPage(BasePage):
    def is_title_matches(self):
        return 'Скачать' in self.driver.title


    def get_win_installer_size(self):
        win_download_link_element = WebDriverWait(self.driver, self.WEBDRIVER_TIMEOUT)\
            .until(EC.presence_of_element_located(SBISDownloadPageLocators.WIN_DOWNLOAD_LINK))
        size = re.search(r'[0-9.]+', win_download_link_element.text)[0]
        return size
    

    def download_installer(self):
        win_download_link_element = WebDriverWait(self.driver, self.WEBDRIVER_TIMEOUT)\
            .until(EC.presence_of_element_located(SBISDownloadPageLocators.WIN_DOWNLOAD_LINK))
        ActionChains(self.driver).move_to_element(win_download_link_element).click().pause(self.WEBDRIVER_ACTION_PAUSE).perform()

    
class SBISDownloadPageLocators(object):
    WIN_DOWNLOAD_LINK = (By.XPATH, '//*[text()="Веб-установщик "]/../..//a')