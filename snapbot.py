from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
import glob
import pickle

chromeOptions = webdriver.ChromeOptions()
dirname = r"E:\Snapchat"
prefs = {"download.default_directory" : dirname}
chromeOptions.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(executable_path=r"chromedriver/chromedriver.exe", options=chromeOptions)

driver.get("file:///C:/Users/Oasis/Downloads/mydata_1635469907106/html/memories_history.html")

sleep(1)

d = "2021-10-25 11-13-42"
d1 = ""
d2 = ""
restart = False

t = driver.find_element_by_xpath('''/html/body/div[2]/table/tbody''')

date_store = open("date_store.pkl", "rb")
links = t.find_elements_by_tag_name("a")
print(len(links))
dates = pickle.load(date_store)
print(len(dates))
date_store.close()

def download_wait(fpath):
    seconds = 0
    dl_wait = True
    while dl_wait and seconds < 60:
        sleep(1)
        dl_wait = False
        for fname in os.listdir(fpath):
            if fname.endswith('.crdownload'):
                dl_wait = True
        seconds += 1
    return seconds

index = 0
for link in links:
    if dates[index] == d:
        print(d, "restarted")
        restart = True
    if restart == True:
        d2 = dates[index]
        d1 = dates[index - 1]
        if d1 != d2:
            link.click()
            sleep(2)
            print(link.get_property("outerHTML"))
            ti = download_wait(dirname)
            if ti == 1:
                filename = max([f for f in os.listdir(dirname)], key=os.path.getctime)
                if filename == dates[index] or filename == dates[index - 1]:
                    continue
            elif ti >= 60:
                print(f"Timeout Error at date: {dates[index]}")
                exit()
            sleep(8)
            filename = max([f for f in os.listdir(dirname)], key=os.path.getctime)
            ext = filename[-3:]
            os.rename(filename, os.path.join(dirname, f"{dates[index]}.{ext}"))
            print(f"{filename} renamed {dates[index]}.{ext}")
            sleep(2)
    index += 1

driver.close()
