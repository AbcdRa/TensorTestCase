from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sbis_contact_page import SBISContactPage
from sbis_main_page import SBISMainPage
from tensor_about_page import TensorAboutPage
from tensor_main_page import TensorMainPage


def test_scenario1_main(webdriver_fixture, driver_setup_func):
    driver = webdriver_fixture
    driver_setup_func(driver)
    driver.get('https://sbis.ru/')
    sbis_main_page = SBISMainPage(driver)
    assert sbis_main_page.is_title_matches()
    sbis_main_page.click_contacts_button()
    sbis_contact_page = SBISContactPage(driver)
    assert sbis_contact_page.is_title_matches()
    assert len(driver.window_handles) == 1
    sbis_contact_page.click_tensor_image()
    assert len(driver.window_handles) == 2
    original_window = driver.current_window_handle

    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
    WebDriverWait(driver, sbis_contact_page.WEBDRIVER_TIMEOUT).until(EC.title_contains('Тензор'))

    tensor_main_page = TensorMainPage(driver)
    assert tensor_main_page.is_title_matches()
    assert tensor_main_page.find_text_blog('Сила в людях')
    tensor_main_page.click_link_more()
    assert driver.current_url == 'https://tensor.ru/about'
    tensor_about_page = TensorAboutPage(driver)
    assert tensor_about_page.is_title_matches()
    images = tensor_about_page.get_working_images()
    assert len(images) > 1
    first_image_size = images[0].size['height'], images[0].size['width']
    for image in images[1:]:
        assert image.size['height'], image.size['width'] == first_image_size


