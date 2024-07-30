from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions as selenium_exception
from base_page import BasePage


class TensorMainPage(BasePage):
    def is_title_matches(self):
        return 'Тензор' in self.driver.title
    

    def find_text_blog(self, contained_text:str):
        try:
            return self.driver.find_element(By.XPATH, f'//*[contains(text(),"{contained_text}")]')
        except selenium_exception.NoSuchElementException:
            return None
    
    
    def click_link_more(self):
        current_url = self.driver.current_url
        element = self.driver.find_element(*TensorMainPageLocators.MORE_LINK_ON_TEXT_BLOCK)
        ActionChains(self.driver).scroll_to_element(element).pause(self.WEBDRIVER_ACTION_PAUSE).scroll_by_amount(0, 200).perform()
        ActionChains(self.driver).pause(self.WEBDRIVER_ACTION_PAUSE).move_to_element(element).click(element).perform()
        WebDriverWait(self.driver, self.WEBDRIVER_TIMEOUT).until(EC.url_changes(current_url))


class TensorMainPageLocators(object):
    MORE_LINK_ON_TEXT_BLOCK = (By.XPATH, '//*[contains(text(),"Сила в людях")]/..//*[text()="Подробнее"]')
