from asyncio.windows_events import NULL
from queue import Empty
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os
import json
import time

browser=webdriver.Chrome()
url="https://www.flipkartcareers.com/#!/joblist"
browser.get(url)



# #to save data to json file

with open("flipcart_data.json","w") as f:
    json.dump([],f)

def save_to_json(new_data,file_name="flipcart_data.json"):
    with open(file_name,"r+") as f:
        file_data=json.load(f)
        file_data.append(new_data)
        f.seek(0)
        json.dump(file_data,f,indent=4)

# for pagination 
isBtnDisabled=False
count=0
while not isBtnDisabled:

    # To get data

    div=[elements for elements in WebDriverWait(browser,10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,'div[class="opening-block wow fadeInUp"]')))]
    for item in div:
        job_title=item.find_element(By.TAG_NAME,'h3').text
        location=item.find_element(By.TAG_NAME,'b').text
        save_to_json({
            "job_title":job_title,
            "location":location,
        })
        try:
            button=WebDriverWait(browser,10).until(EC.visibility_of_element_located((By.XPATH,'//div/button[@class="loadmore-btn"]')))
            if not(button==NULL):
                browser.find_element(By.XPATH,'//div/button[@class="loadmore-btn"]')
            else:
                print(button==NULL)
                isBtnDisabled=True
                break
        except  Exception as e:
            print("--------- error--------")
        
time.sleep(5)
browser.close()


