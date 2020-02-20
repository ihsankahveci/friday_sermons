from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
#import time  #necessary for time.sleep()

option = webdriver.ChromeOptions()
option.add_argument("--incognito ")
option.add_argument("--kiosk") #open in full screen to prevent click error

browser = webdriver.Chrome(
    executable_path= '/Users/ihsankahveci/Desktop/Sermon_Scraper/friday_sermons/sermon_scraper/chromedriver', 
    chrome_options=option
)

URL = "https://www2.diyanet.gov.tr/DinHizmetleriGenelMudurlugu/Sayfalar/HutbelerListesi-Ingilizce.aspx?" 
browser.get(URL)
'''
Qhile loop iterates over pages,
For loop gets the sermon links in that page.
'''
links = []
running = True
page = 1
while running:
    for row in range(2, 12):
        PATH = "//*[@id='onetidDoclibViewTbl0']/tbody/tr[" + str(row) + "]/td[3]/a"
        links_element = browser.find_elements_by_xpath(PATH)  #find_elements_by_xpath returns an array of selenium objects.

        try:
            links.append(links_element[0].get_attribute('href'))  #[0] gives the element in the selenium object. 
        except:
            running = False
    if page == 1:                         #first page does not have a back button, hence the next button is 2nd td.
        page_element = browser.find_elements_by_xpath("//*[@id='bottomPagingCellWPQ2']/table/tbody/tr/td[2]/a/img")    
        button = page_element[0]
        button.click()
    else:
        page_element = browser.find_elements_by_xpath("//*[@id='bottomPagingCellWPQ2']/table/tbody/tr/td[3]/a/img")    
        button = page_element[0] 
        button.click()
    
    browser.implicitly_wait(10)
    #time.sleep(10) 
    print(browser.current_url) #to keep track of the progress
    if page == 50:             #50 is an arbitrary number
        break
    else: 
        page = page +  1
    
browser.close() 
with open('sermons.txt', 'w') as filehandle:                #writing links into a txt document.
    filehandle.writelines("%s\n" % link for link in links)

