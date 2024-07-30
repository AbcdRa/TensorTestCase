from sbis_contact_page import SBISContactPage


def test_scenario_main(webdriver_fixture, driver_setup_func):
    driver = webdriver_fixture
    driver_setup_func(driver)
    driver.get('https://sbis.ru/contacts')
    sbis_contact_page = SBISContactPage(driver)
    assert sbis_contact_page.get_region_name() == 'Тюменская обл.'
    assert sbis_contact_page.has_partners_list()
    tyumen_partner_set = set(sbis_contact_page.get_partner_list())
    sbis_contact_page.change_region_name("Камчатский край")
    assert sbis_contact_page.get_region_name() == 'Камчатский край'
    assert sbis_contact_page.has_partners_list()
    kamchatka_partner_set = set(sbis_contact_page.get_partner_list())
    assert len(tyumen_partner_set & kamchatka_partner_set) != len(tyumen_partner_set)
    assert driver.current_url[:driver.current_url.find('?')] == 'https://sbis.ru/contacts/41-kamchatskij-kraj'
    assert 'Камчатский край' in driver.title