from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
import pickle

dirname = r"E:\Snapchat"
driver = webdriver.Chrome(executable_path=r"chromedriver/chromedriver.exe")

driver.get("file:///C:/Users/Oasis/Downloads/mydata_1635469907106/html/memories_history.html")

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