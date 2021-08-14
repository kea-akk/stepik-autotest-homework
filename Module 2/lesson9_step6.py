from selenium import webdriver 

# Для операций времени вызвать
import time
# Для сложных математических операций вызвать
import math

try: 
    def calc(x): 
        return str(math.log(abs(12*math.sin(int(x)))))

    link = "http://suninjuly.github.io/redirect_accept.html"

    browser = webdriver.Chrome()
    browser.get(link)

    # Найти кнопку и нажать
    browser.find_element_by_tag_name("button").click()

    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_elt = browser.find_element_by_id("input_value")
    x = x_elt.text
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    # Найти кнопку и нажать
    browser.find_element_by_tag_name("button").click()
finally: 
    time.sleep(5)
    browser.quit()
