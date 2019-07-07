from selenium import webdriver
import math


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)
x = browser.find_element_by_id("treasure").get_attribute("valuex")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser.find_element_by_id("answer").send_keys(calc(x))

browser.find_element_by_id("robotsRule").click()

browser.find_element_by_id("robotCheckbox").click()

browser.find_element_by_tag_name("button").click()
