import time

from selenium import webdriver

try:
    #link = "http://suninjuly.github.io/selects1.html"
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # находим элемент, содержащий текст
    num1_elt = browser.find_element_by_id("num1")
    # записываем в переменную num1 текст из элемента num1_elt
    num1 = int(num1_elt.text)
    # находим элемент, содержащий текст
    num2_elt = browser.find_element_by_id("num2")
    # записываем в переменную num2 текст из элемента num2_elt
    num2 = int(num2_elt.text)    

    summa = str(num1 + num2)
    
    ''' # выбор элемента из списка через Select
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(summa) # ищем элемент с текстом равным строке из переменной summa   
    '''
    
    # выбор элемента из списка через селекторы
    browser.find_element_by_tag_name("select").click()
    # подставляем переменную в конструкцию browser.find_element_by_css_selector("[value='1']").click() через конкатенацию строк:
    browser.find_element_by_css_selector("[value='" + summa + "']").click()
    
    browser.find_element_by_tag_name("button").click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
