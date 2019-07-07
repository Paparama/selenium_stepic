import time
from telnetlib import EC

from selenium import webdriver
import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from selenium.webdriver.support.wait import WebDriverWait

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)
price = WebDriverWait(browser, 15).until(
  text_to_be_present_in_element((By.ID, "price"), "10000 RUR")
    )
browser.find_element_by_id("book").click()


x = browser.find_element_by_id("input_value").text

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser.find_element_by_class_name("form-control").send_keys(calc(x))

browser.find_element_by_id("solve").click()

