from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

driver = webdriver.Firefox(executable_path='geckodriver.exe')

# change link 
driver.get("https://www.adobe.com/404")

elems = driver.find_elements(By.XPATH, "//a[@href]")
for elem in elems:
    if (requests.get(elem.get_attribute("href")).status_code) != 200:
        print("Error: " + elem.get_attribute("href"))
