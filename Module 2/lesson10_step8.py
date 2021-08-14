# конструкция для работы метода By и ожидания с ожидаемыми условиями
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# сокращаем импортированный метод до двух букв для простоты кода
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
import math
import time

def calc(x): 
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
 
browser = webdriver.Chrome()
browser.get(link)

# говорим Selenium проверять в течение 12 секунд, пока текст не сравняется с заданным
text = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"100")
    )
# найти кнопку Book
browser.find_element_by_id("book").click()

x_elt = browser.find_element_by_id("input_value")
x = x_elt.text
y = calc(x)

input1 = browser.find_element_by_id("answer")
input1.send_keys(y)

# Найти кнопку и нажать
browser.find_element_by_id("solve").click()

time.sleep(5)
browser.quit()
