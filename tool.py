import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

'''CHROMEDRIVER SETUP'''

c_options=Options() # create options object for chrome
#c_options.add_argument('--headless')   # to scrape web without displaying window

s = Service(ChromeDriverManager().install())    # set up manager service for chromedriver
browser = webdriver.Chrome(service = s)#, options = c_options) # instantiate chromedriver
# Nike resources
nikeSNKRSfeed = 'https://www.nike.com/launch'
nikeSNKRSinstock = 'https://www.nike.com/launch?s=in-stock'
nikeSNKRSupcoming = 'https://www.nike.com/launch?s=upcoming'
nikeTWITTER = 'https://twitter.com/nikestore'   #Twitter link

shoe_keyword = input('enter a keyword to search for: ')   #enter keyword of shoe you are trying to get
##############################################################
def search(link: str) -> bool:
    browser.get(link)
    time.sleep(1)
    source = browser.page_source
    shoe_found = shoe_keyword in source
    if(shoe_found):
        print('found shoes!')
        return
    else:
        browser.refresh()
##############################################################
#browser.maximize_window() # For maximizing window

while True:
    time.sleep(1)
    search(nikeSNKRSfeed)
    search(nikeSNKRSinstock)
    search(nikeSNKRSupcoming)
    time.sleep(4) #refreshes every 5 seconds
browser.quit()
'''
while True: #press on tweet
    try:
        tweet = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[1]').click()
        break
    except:
        pass
while True:
    try:  #searches for link in element
        find_href = browser.find_element(By.CSS_SELECTOR, '.css-4rbku5.css-18t94o4.css-901oao.css-16my406.r-1cvl2hr.r-1loqt21.r-poiln3.r-bcqeeo.r-qvutc0')
        print(find_href.get_attribute('href')) #find link inside element
        break
    except:
        pass
'''
