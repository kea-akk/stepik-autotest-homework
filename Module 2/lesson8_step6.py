import time
import math 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

from selenium import webdriver

try:
    link = "http://suninjuly.github.io/execute_script.html"

    browser = webdriver.Chrome()
    browser.get(link)

    x_elt = browser.find_element_by_id("input_value")
    x = x_elt.text
    y = calc(x) 

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    check1 = browser.find_element_by_id("robotCheckbox").click()
    check2 = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", check2) # скрытый за футером элемент поднять в зону видимости
    check2.click()

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button) # скрытый за футером элемент поднять в зону видимости
    button.click()
finally:
    time.sleep(5)
    browser.quit()
