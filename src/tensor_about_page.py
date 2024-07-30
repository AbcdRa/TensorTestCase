from selenium.webdriver.common.by import By
from base_page import BasePage


class TensorAboutPage(BasePage):
    def is_title_matches(self):
        return 'О компании' in self.driver.title


    def get_working_images(self):
        elements = self.driver.find_elements(*TensorAboutPageLocators.WORKING_IMAGES)
        return elements


class TensorAboutPageLocators(object):
    WORKING_IMAGES = (By.XPATH, '//*[contains(text(),"Работаем")]/../..//img')

