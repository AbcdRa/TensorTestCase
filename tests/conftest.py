from pathlib import Path
import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
import os


@pytest.fixture(scope='session', autouse=True)
def webdriver_fixture(pytestconfig):
    download_folder_path =str(pytestconfig.rootpath.joinpath('downloads'))
    options = webdriver.ChromeOptions()
    options.add_argument('--log-level=3')
    options.add_argument('--disable-features=InsecureDownloadWarnings')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--unsafely-treat-insecure-origin-as-secure=http://*.sbis.ru')
    options.add_experimental_option('prefs', {
        'download.default_directory':download_folder_path,
        'download.prompt_for_download': False,
        'download.directory_upgrade': True,
        "safebrowsing.enabled": True})
    driver = webdriver.Chrome(options=options)
    driver.download_folder_path = download_folder_path
    yield driver
    driver.close()


@pytest.fixture(scope='function', autouse=True)
def driver_setup_func():
    def driver_setup(driver:WebDriver):
        curr=driver.current_window_handle
        for handle in driver.window_handles:
            driver.switch_to.window(handle)
            if handle != curr:
                driver.close()
        driver.switch_to.window(driver.current_window_handle)
        for file in Path(driver.download_folder_path).glob('**/*'):
            os.remove(file)

    return driver_setup