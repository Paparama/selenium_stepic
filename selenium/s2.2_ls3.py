from selenium import webdriver
import os

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

[elem.send_keys("some txt") for elem in browser.find_elements_by_tag_name("input")[:3]]

browser.find_element_by_id("file").send_keys(file_path)

browser.find_element_by_tag_name("button").click()