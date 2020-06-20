from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json;
chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options)
browser.get('http://placement.bitmesra.ac.in/')
inputt = browser.find_element_by_xpath('//*[@id="txtUsername"]')
inputt.send_keys("amankumarsingh@outlook.in")
password = browser.find_element_by_xpath('//*[@id="txtPassword"]')
password.send_keys("g#gVq8^W")
Button = browser.find_element_by_xpath('//*[@id="imgSubmit"]')
Button.click()
data = browser.find_elements_by_class_name('col-xs-12')
d = []
for items in data:
    d.append(items.text)

# datas = json.load(d)
print(d);
