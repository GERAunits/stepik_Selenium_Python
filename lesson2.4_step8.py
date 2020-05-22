from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
WebDriverWait(browser, 10).until(
    EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
)

browser.find_element_by_css_selector('#book').click()

x = browser.find_element_by_css_selector('#input_value').text
y = str(math.log(abs(12*math.sin(int(x)))))

browser.find_element_by_css_selector('#answer').send_keys(y)
browser.find_element_by_css_selector('#solve').click()
