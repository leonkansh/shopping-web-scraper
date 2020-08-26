def searchBestBuy(search, BeautifulSoup, driver):
    # BestBuy
    print('Gathering Best Buy listings...')
    URL_bb = 'https://www.bestbuy.com/site/searchpage.jsp?st=' + search
    driver.get(URL_bb)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    results = soup.find(class_='col-xs-9')
    listings = results.find_all('div', class_='right-column')
    # loops all the BestBuy results twice
    # extract the element name and price from the listing by find the HTML
    runs = 0
    for listing in listings:
        if runs >= 1: break
        item_element = listing.find('h4', class_='sku-header')
        item_price = listing.find('span', class_='aria-hidden')
        if None in (item_element, item_price): continue
        print(item_element.text.strip())
        print(item_price.text.strip())
        print()
        print()
        runs += 1;

    # find elements thru entire list by class
    # ex. soup.findAll('<tag>', attrs = {'class' : '<classname>'})
    # results = soup.findAll('h4', attrs={'class': 'sku-header'})
    # # results = soup.findAll('a', href="site/bose-soundlink-color-portable-bluetooth-speaker-ii-soft-black/5520801.p?skuId=5520801")
    # for listing in results:
    #     if runs >= 1: break
    #     print(soup.select_one('h4.sku-header').get_text())
    #     runs += 1

    # runs = 0
    # results = soup.findAll('div', attrs = {'class': 'priceView-hero-price priceView-customer-price'})
    # for listing in results:
    #     if runs >= 1: break
    #     element = soup.select_one('div.priceView-customer-price)') 
    #     #  > span:first-child
    #     #finds only the first tag that matches a selector
    #     if None in element:
    #         continue
    #     print(element.get_text())
    #     print()
    #     print()
    #     runs += 1

    # save price
    bb_price = item_price.text.strip()
    bb_price = bb_price.replace('$', '')
    bb_price = float(bb_price)