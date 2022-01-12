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

link = 'https://twitter.com/nikestore'   #Twitter link
shoe_keyword = 'Crimson'   #enter keyword of shoe you are trying to get
#browser.maximize_window() # For maximizing window

browser.get(link)

while True:
    time.sleep(1)
    source = browser.page_source #downloads page source
    shoe_live = shoe_keyword in source  #checks page source for shoe using keywords

    if shoe_live == True:
        print('Found shoes')  #exits loop continues on to fetch link
        break
    else:
      browser.refresh()   #refresh browser
    time.sleep(14) #refreshes every 15 seconds


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
