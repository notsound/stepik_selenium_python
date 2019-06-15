from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x_element):
  return str(math.log(abs(12*math.sin(int(x_element)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.ID,"book")
price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR")
    )
button.click()

x_element = browser.find_element(By.ID, "input_value").text
result = calc(int(x_element))


answer = browser.find_element_by_id("answer").send_keys(result)

button = browser.find_element_by_id("solve")
button.click()

