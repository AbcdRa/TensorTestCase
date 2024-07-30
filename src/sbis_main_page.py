from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from base_page import BasePage


class SBISMainPage(BasePage):
    def is_title_matches(self):
        return 'СБИС — экосистема для бизнеса: учет, управление и коммуникации' == self.driver.title


    def click_contacts_button(self):
        element = self.driver.find_element(*SBISMainPageLocators.CONTACTS_BUTTON)
        ActionChains(self.driver).move_to_element(element).click().perform()
        WebDriverWait(self.driver, self.WEBDRIVER_TIMEOUT).until(EC.title_contains('Контакты'))


    def click_download_link(self):
        self.driver.implicitly_wait(self.WEBDRIVER_TIMEOUT)
        element = WebDriverWait(self.driver, self.WEBDRIVER_TIMEOUT)\
            .until(EC.presence_of_element_located(SBISMainPageLocators.DOWNLOAD_LINK))
        ActionChains(self.driver).move_to_element(element).click().perform()
        WebDriverWait(self.driver, self.WEBDRIVER_TIMEOUT).until(EC.title_contains('Скачать'))


class SBISMainPageLocators(object):
    CONTACTS_BUTTON = (By.LINK_TEXT, 'Контакты')
    DOWNLOAD_LINK = (By.LINK_TEXT, 'Скачать локальные версии')