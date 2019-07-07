import time

from selenium import webdriver
import math


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)
browser.find_element_by_tag_name("button").click()
wind = browser.window_handles[1]

browser.switch_to.window(wind)


x = browser.find_element_by_id("input_value").text

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser.find_element_by_class_name("form-control").send_keys(calc(x))

browser.find_element_by_tag_name("button").click()
