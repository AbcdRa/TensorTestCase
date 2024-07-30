from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_page import BasePage


class SBISContactPage(BasePage):
    def is_title_matches(self):
        return 'Контакты' in self.driver.title
    

    def get_region_name(self):
        region_element = WebDriverWait(self.driver, self.WEBDRIVER_TIMEOUT)\
            .until(EC.presence_of_element_located(SBISContactPageLocators.REGION_TEXT))
        return region_element.text


    def change_region_name(self, region_name:str):
        region_text = self.driver.find_element(*SBISContactPageLocators.REGION_TEXT)
        ActionChains(self.driver).move_to_element(region_text).click().perform()
        new_region_item = WebDriverWait(self.driver, self.WEBDRIVER_TIMEOUT)\
            .until(EC.presence_of_element_located(SBISContactPageLocators.get_region_item(region_name)))
        ActionChains(self.driver).move_to_element(new_region_item).click().pause(self.WEBDRIVER_ACTION_PAUSE).perform()


    def get_partner_list(self):
        contact_item_list_raw = self.driver.find_elements(*SBISContactPageLocators.CONTACTS_ITEM_LIST)
        return list(map(lambda it: tuple(it.text.split('\n')), contact_item_list_raw))


    def has_partners_list(self):
        return "В этом регионе пока нас нет." not in self.driver.find_element(*SBISContactPageLocators.CONTACTS_LIST).text


    def click_tensor_image(self):
        current_tabs_count = len(self.driver.window_handles)
        element = self.driver.find_element(*SBISContactPageLocators.TENSOR_IMAGE)
        ActionChains(self.driver).move_to_element(element).pause(self.WEBDRIVER_ACTION_PAUSE).click().perform()
        WebDriverWait(self.driver, self.WEBDRIVER_TIMEOUT).until(EC.number_of_windows_to_be(current_tabs_count+1))


class SBISContactPageLocators(object):
    TENSOR_IMAGE = (By.XPATH, '//img[contains(@alt, "Тензор")]')  
    REGION_TEXT = (By.XPATH, '//*[contains(@class,"sbis_ru-Region-Chooser__text")]')
    CONTACTS_LIST = (By.XPATH, '//*[contains(@class, "sbisru-Contacts-List__col ")]')
    CONTACTS_ITEM_LIST = (By.XPATH, '//*[contains(@class, "sbisru-Contacts-List__col-1")]')
    get_region_item = lambda region_name: (By.XPATH, 
                                          f'//div[contains(@class,"sbis_ru-Region-Panel")]//*[contains(text(),"{region_name}")]')   
