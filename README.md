# Best Deal Finder
### What is Best Deal Finder?
is a Python console app that finds the lowest price among the largest E-commerce companies, like Amazon, eBay, and BestBuy by utilizing Beautiful Soup and Selenium.

### Setup
- Download and install Python
Once you download the repository and ready to go on your terminal, type the following in your terminal:
Windows:

`sudo apt update && upgrade`

`sudo apt install python3 python3-pip ipython3`


Mac: 

`brew install python`

- Download and install libraries
Then copy and paste the next command lines to your terminal:

`pip3 install requests`

`pip3 install beautifulsoup4`

### Running the program!
You are almost ready to go, type the following to your terminial

`python3 main.py`

### Troubleshooting
- What if the program doesn't run?

If the program doesn't run, make sure you choose Google Chrome as your default browswer. 
- Error message?

If you received an error message says, `selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 84`, or something like that, make sure you use the correct version of ChromeDriver. The correct version in this respository works for Chrome 
Version 85 64-bit Mac OS. 

Here is a [link](https://sites.google.com/a/chromium.org/chromedriver/downloads) to update your ChromeDriver. 
After you have downloaded the right version, make sure to replace the _old_ [chromedriver](https://github.com/leonkansh/shopping-web-scraper/blob/master/chromedriver) in the **shopping-web-scraper** folder.
