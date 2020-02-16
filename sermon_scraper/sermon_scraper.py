from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException

option = webdriver.ChromeOptions()
option.add_argument("--incognito")

browser = webdriver.Chrome(executable_path= '../sermon_scraper/chromedriver', chrome_options=option)
browser.get('https://www2.diyanet.gov.tr/DinHizmetleriGenelMudurlugu/Sayfalar/HutbelerListesi-Ingilizce.aspx')

# # Wait 2 seconds to make sure the page loads completely. 
# timeout = 2
# try:
#     WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, “//img[@class=’avatar width-full rounded-2']”)))
# except TimeoutException:
#     print(“Timed out waiting for page to load”)
#     browser.quit()


# find_elements_by_xpath returns an array of selenium objects.
links = []
for i in range(2, 12):
    PATH = "//*[@id='onetidDoclibViewTbl0']/tbody/tr[" + str(i) + "]/td[3]/a"
    
    #find_elements_by_xpath returns an array of selenium objects.
    links_element = browser.find_elements_by_xpath(PATH)    
    links.append(links_element[0].get_attribute('href'))


# print out all the links.
print(*links, sep = '\n')

browser.close()
