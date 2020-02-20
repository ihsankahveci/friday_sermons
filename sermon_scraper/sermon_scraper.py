from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import time 

option = webdriver.ChromeOptions()
option.add_argument("--incognito")

browser = webdriver.Chrome(
    executable_path= '/Users/ihsankahveci/Desktop/Sermon_Scraper/friday_sermons/sermon_scraper/chromedriver', 
    chrome_options=option
)

URL = "https://www2.diyanet.gov.tr/DinHizmetleriGenelMudurlugu/Sayfalar/HutbelerListesi-Ingilizce.aspx?" 
browser.get(URL)

links = []

for page in range(1, 30):

    for row in range(2, 12):
        PATH = "//*[@id='onetidDoclibViewTbl0']/tbody/tr[" + str(row) + "]/td[3]/a"
        #find_elements_by_xpath returns an array of selenium objects.
        links_element = browser.find_elements_by_xpath(PATH)    
        links.append(links_element[0].get_attribute('href'))

    if page == 1:
        page_element = browser.find_elements_by_xpath("//*[@id='bottomPagingCellWPQ2']/table/tbody/tr/td[2]/a/img")    
        button = page_element[0] #.get_attribute('img')
        button.click()

    else:
        page_element = browser.find_elements_by_xpath("//*[@id='bottomPagingCellWPQ2']/table/tbody/tr/td[3]/a/img")    
        button = page_element[0] #.get_attribute('img')
        button.click()
    
    #browser.implicitly_wait(30)
    time.sleep(5)
        
    print(browser.current_url)

browser.close()


with open('sermons.txt', 'w') as filehandle:
    filehandle.writelines("%s\n" % place for link in links)

#print(*links, sep = '\n')

# /Users/ihsankahveci/Desktop/Sermon_Scraper/friday_sermons/sermon_scraper/chromedriver
# # Wait 2 seconds to make sure the page loads completely. 
# timeout = 2
# try:
#     WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, “//img[@class=’avatar width-full rounded-2']”)))
# except TimeoutException:
#     print(“Timed out waiting for page to load”)
#     browser.quit()


# find_elements_by_xpath returns an array of selenium objects.


# print out all the links.
