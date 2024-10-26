from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
import pickle

dirname = r"<path-to-output-files>"
driver = webdriver.Chrome(executable_path=r"<path-to-chromedriver-executable>")

driver.get("<path-to-input-html-file>")

sleep(1)

date_store = open("date_store.pkl", "wb")

t = driver.find_element_by_xpath('''/html/body/div[2]/table/tbody''')
cols = t.find_elements_by_tag_name("td")
print(len(cols))
dates = [i.text[:-4].replace(":", "-") for i in cols if "UTC" in i.text]
print(len(dates))
pickle.dump(dates, date_store)
date_store.close()

driver.close()