# libraries
import requests
from bs4 import BeautifulSoup # pass in the HTML source from webdriver into it to parse.
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from requests_html import HTMLSession
import os

# dictionary
headers = {
    'Host': 'www.amazon.com',
    # find user-agent by search "user agent checker"
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'TE': 'Trailers'
}

# launch Chrome (create an instance of Chrome webdriver)
# instantiate a chrome options object so you can set the size and headless preference
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

# download the chrome driver from https://sites.google.com/a/chromium.org/chromedriver/downloads and put it in the
# current directory
chrome_driver = os.getcwd() +"/chromedriver"

driver = webdriver.Chrome('/Users/kanyuanliang/Documents/GitHub/web-scraper/chromedriver')

# Getting user input
search = input('Enter the item you want to search for: ')
print()
print('Searching for ' + search)

# replace all the 'spaces' in userInput by a '+'
search = search.replace(' ', '+') # query parameters

# eBay:
# print('Gathering eBay listings...')
# URL_e = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313.TR12.TRC2.A0.H0.XApple+iPhone.TRS0&_nkw=' + search
# page = requests.get(URL_e)

# # parse this downloaded HTML (BeautifulSoup provides to scrape text from this object)
# soup = BeautifulSoup(page.content, 'html.parser')
# # filtering
# results = soup.find(id='mainContent')
# # find items based on class
# # li tags(the listings), s-item(class attribute)
# listings = results.find_all('li', class_='s-item')

# runs = 0
# for listing in listings:
#     if runs >= 1: break
#     item_element = listing.find('h3', class_='s-item__title')
#     item_price = listing.find('span', class_='s-item__price')
#     if None in (item_element, item_price):
#         continue
#     print(item_element.text.strip()) #why strip(): remove extraneous characters
#     print(item_price.text.strip())
#     print()
#     print()
#     runs += 1
# # save price
# eBay_price = item_price.text.strip()
# eBay_price = eBay_price.replace('$', '')
# eBay_price = float(eBay_price)
# [0:5:1]


# Amazon:
print('Gathering Amazon listings...')
URL = 'https://www.amazon.com/s?k=' + search
# get and search URL
page = driver.get(URL)
# parse this downloaded HTML
soup = BeautifulSoup(driver.page_source, 'html.parser')
# results = soup.findAll('span', attrs={'class': 'a-size-medium a-color-base a-text-normal'})
results = soup.find(class_='s-desktop-width-max s-opposite-dir')
listing = results.find_all('div', class_='s-include-content-margin s-border-bottom s-latency-cf-section')

runs = 0
# for listing in results:
for listing in listings:
    if runs >= 1: break
    item_element = listing.find('span', class_='a-size-medium a-color-base a-text-normal')
    item_price = listing.find('span', class_='a-offscreen')
    if None in (item_element, item_price): continue
    print(item_element.text.strip()) #why strip(): remove extraneous characters
    print(item_price.text.strip())
    print()
    print()
    # print(soup.select_one('span.a-size-medium').get_text())
    runs += 1;

# runs = 0
# results = soup.findAll('span', attrs={'class': 'a-offscreen'})
# for listing in results:
#     if runs >= 1: break
#     element = soup.select_one('span.a-offscreen')
#     if None in element:
#         continue
#     print(element.get_text())
#     print()
#     print()
#     runs += 1

# save the price
amazon_price = item_price.text.strip() # call strip() to remove extraneous characters
amazon_price = amazon_price.replace('$', '') # then we can do math operation/comparsion
amazon_price = float(amazon_price)


# BestBuy
print('Gathering Best Buy listings...')
URL_bb = 'https://www.bestbuy.com/site/searchpage.jsp?st=' + search
driver.get(URL_bb)

# loops all the BestBuy results twice
# extract the element name and price from the listing by find the HTML
runs = 0
# find elements thru entire list by class
# ex. soup.findAll('<tag>', attrs = {'class' : '<classname>'})
results = soup.findAll('h4', attrs={'class': 'sku-header'})
# results = soup.findAll('a', href="site/bose-soundlink-color-portable-bluetooth-speaker-ii-soft-black/5520801.p?skuId=5520801")
for listing in results:
    if runs >= 1: break
    print(soup.select_one('h4.sku-header').get_text())
    runs += 1

runs = 0
results = soup.findAll('div', attrs = {'class': 'priceView-hero-price priceView-customer-price'})
for listing in results:
    if runs >= 1: break
    element = soup.select_one('div.priceView-customer-price)') 
    #  > span:first-child
    #finds only the first tag that matches a selector
    if None in element:
        continue
    print(element.get_text())
    print()
    print()
    runs += 1

# save price
bb_price = item_price.text.strip()
bb_price = bb_price.replace('$', '')
bb_price = float(bb_price)


# price comparison
print('Comparing the three prices...')

elected_link = ''
elected_price = 0.00

if (eBay_price <= amazon_price) and (eBay_price <= bb_price):
    elected_price = eBay_price
    elected_link = URL_e
elif (amazon_price <= eBay_price) and (amazon_price <= bb_price):
    elected_price = amazon_price
    elected_link = URL
elif (bb_price <= amazon_price) and (bb_price <= eBay_price):
    elected_price = bb_price
    elected_link = URL_bb

print('Here\'s the link to the lowest price. Have fun!')
print(elected_link)
print('$' + str(elected_price))