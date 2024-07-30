from selenium.webdriver.support.wait import WebDriverWait
from pathlib import Path
import os
from sbis_download_page import SBISDownloadPage
from sbis_main_page import SBISMainPage

def test_scenario3(webdriver_fixture, driver_setup_func):
    driver = webdriver_fixture
    driver_setup_func(driver)
    driver.get('https://sbis.ru/')
    sbis_main_page = SBISMainPage(driver)
    sbis_main_page.click_download_link()
    sbis_download_page = SBISDownloadPage(driver)
    assert sbis_download_page.is_title_matches()
    expected_installer_size = sbis_download_page.get_win_installer_size()
    sbis_download_page.download_installer()
    WebDriverWait(driver, 10)\
        .until(lambda d: "sbisplugin-setup-web.exe" in map(lambda p: p.name, Path(driver.download_folder_path).glob('**/*')))
    filenames = map(lambda p: p.name, Path(driver.download_folder_path).glob('**/*'))
    assert "sbisplugin-setup-web.exe" in filenames
    plugin_path = Path(driver.download_folder_path).joinpath("sbisplugin-setup-web.exe")

    #Получаем размер в мегабайтах, округляем до точности в 2 цифры после запятой
    plugin_size = str(round(os.path.getsize(plugin_path)/1024/1024,2)) 
    assert plugin_size == expected_installer_size
                

