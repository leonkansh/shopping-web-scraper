def searcheBay(search, requests, BeautifulSoup):
    print('Gathering eBay listings...')
    URL_e = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313.TR12.TRC2.A0.H0.XApple+iPhone.TRS0&_nkw=' + search
    page = requests.get(URL_e)

    # parse this downloaded HTML (BeautifulSoup provides to scrape text from this object)
    soup = BeautifulSoup(page.content, 'html.parser')
    # filtering
    results = soup.find(id='mainContent')
    # find items based on class
    # li tags(the listings), s-item(class attribute)
    listings = results.find_all('li', class_='s-item')

    runs = 0
    for listing in listings:
        if runs >= 1: break
        item_element = listing.find('h3', class_='s-item__title')
        item_price = listing.find('span', class_='s-item__price')
        if None in (item_element, item_price):
            continue
        print(item_element.text.strip()) #why strip(): remove extraneous characters
        print(item_price.text.strip())
        print()
        print()
        runs += 1
    # save price
    eBay_price = item_price.text.strip()
    eBay_price = eBay_price.replace('$', '')
    eBay_price = float(eBay_price)

    return eBay_price, URL_e