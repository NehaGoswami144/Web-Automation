from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as E
from selenium.webdriver.support import expected_conditions as EC


import openpyxl
from openpyxl import load_workbook

wrkbuk= openpyxl.Workbook()
s=wrkbuk.active
head=['Python_developer_from_london_profile']
s.append(head)
##wrkbuk.save('neha2.xlsx')
path2=r"C:\Users\HP\AppData\Local\Programs\Python\Python310\Lib\site-packages\aws_lib_\web.xlsx"





path=(r'‪chromedriver.exe')
driver=webdriver.Chrome()
driver.get('https://www.google.co.in/')

username=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'))).send_keys('linkedin python developer profiles from london')
search=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[2]/ul[1]/div/ul/li[1]/div/div[2]'))).click()



data_dict={}
for i in range(0,4):
    Python_developer_from_london_profile=WebDriverWait(driver,50).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div['+str(i+1)+']/div/div[1]/div/a/h3'))).text    
##    item=item.split('\n')
    print(Python_developer_from_london_profile)
    print(i)
    data_dict['Python developer from london profile']=Python_developer_from_london_profile

    lis_data=[data_dict['Python developer from london profile']]
    print(lis_data)
    
    s.append(lis_data)
    wrkbuk.save(path2)
