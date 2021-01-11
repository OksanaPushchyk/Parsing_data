#!/usr/bin/env python
# coding: utf-8

# In[12]:


from selenium import webdriver
from bs4 import BeautifulSoup
import time

pair = 'LINK'
url = 'https://futures.huobi.com/en-us/linear_swap/info/swap_fee/#symbol=%s' %(pair)

browser = webdriver.Chrome('P:/Downloads/chromedriver.exe')
browser.get(url)
#print(browser.page_source)

source = browser.page_source

soup = BeautifulSoup(source, 'html.parser')

number_of_pages = browser.find_element_by_xpath("//div[@class='pagination pagination-root  secondary-font']")
n = int(number_of_pages.text[number_of_pages.text.find('/') + 1 : number_of_pages.text.find(' ')])
print('n = ', n)

data = []

for i in range(n):
    m = i + 1
    print(i, m)
    
    elements = browser.find_elements_by_xpath("//tr[@class='table-body-line number-font']")
    for j in range(len(elements)):
        data.append(elements[j].text)
    
    page_number = browser.find_element_by_xpath("//input[@class='input pagination-input']")
    page_number.clear()
    page_number.send_keys(m)
    
    time.sleep(2)
    
    #<button disabled="" class="pagination-confirm blue-background pagination-button">Confirm</button>
    #<button class="border-input pagination-arrow pagination-button"><span class="arrow arrow-next border-secondary"></span></button>
    
    button = browser.find_element_by_xpath("//button[@class='pagination-confirm blue-background pagination-button']")
    button.click()
    time.sleep(2)
    
elements = browser.find_elements_by_xpath("//tr[@class='table-body-line number-font']")
for j in range(len(elements)):
    data.append(elements[j].text)
    
    
import csv

with open(pair + '_hiobi.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    for item in data:
        csv_writer.writerow([item])


# In[13]:


data


# In[4]:


import csv

with open('hiobi.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    for item in data:
        csv_writer.writerow([item])

