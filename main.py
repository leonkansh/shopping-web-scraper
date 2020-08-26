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

# ----call the functions----
from ebay import searcheBay
eBay_price, URL_e = searcheBay(search, requests, BeautifulSoup)

from amazon import searchAmazon
amazon_price, URL = searchAmazon(search, requests, BeautifulSoup, driver)

# from bestbuy import searchBestBuy
# searchBestBuy(search, BeautifulSoup, driver)

from price_comparison import comparePrices
comparePrices(eBay_price, amazon_price, URL_e, URL)