from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
#import time  #necessary for time.sleep()

option = webdriver.ChromeOptions()
option.add_argument("--incognito ")
option.add_argument("--kiosk")     #open in full screen to prevent click error

browser = webdriver.Chrome(
    executable_path= '/Users/ihsankahveci/Desktop/Sermon_Scraper/friday_sermons/sermon_scraper/chromedriver', 
    chrome_options=option
)

URL = "https://www2.diyanet.gov.tr/DinHizmetleriGenelMudurlugu/Sayfalar/HutbelerListesi-Ingilizce.aspx?" 


browser.get(URL)


links_element = browser.find_elements_by_xpath("//*[@id='onetidDoclibViewTbl0']/tbody/tr")

for i in range(0, len(links_element)):
    print(links_element[i].get_attribute('td'))

#onetidDoclibViewTbl0 > tbody > tr:nth-child(2) > td:nth-child(3) > a

browser.close()




# for row in range(2, maxRow):
#             PATH = "//*[@id='onetidDoclibViewTbl0']/tbody/tr[" + str(row) + "]/td[3]/a"
#             links_element = browser.find_elements_by_xpath(PATH)    #find_elements_by_xpath returns an array of selenium objects.
#             try:
#                 links.append(links_element[0].get_attribute('href'))    #[0] gives the element in the selenium object. 
#             except:
#                 print(*links, sep='\n')
#                 running = False