from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

driver = webdriver.Firefox(executable_path='geckodriver.exe')

# change link 
links = ["https://www.drlinkcheck.com/"]

count = 0


for link in links:
    driver.get(link)
    count += 1
    elems = driver.find_elements(By.XPATH, "//a[@href]")
    for elem in elems:
        if "mailto" not in elem.get_attribute("href"):
            links.append(elem.get_attribute("href"))
            if (requests.get(elem.get_attribute("href")).status_code) != 200:
                print("Error: " + elem.get_attribute("href"))

    links.remove(link)

    if count > 5:
        print("Max depth exceeded")
        break
    #print(links)
