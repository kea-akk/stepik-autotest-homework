import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_element_by_xpath('//button[contains(@class, "btn-add-to-basket")]')
    assert button.get_attribute('type') == 'submit', 'Кнопка "Добавить в корзину" не найдена'
