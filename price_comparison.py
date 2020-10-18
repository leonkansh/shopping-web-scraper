def comparePrices(eBay_price, amazon_price, URL_e, URL):
    print()
    print('Comparing the three prices...')

    elected_link = ''
    elected_price = 0.00

    if (eBay_price <= amazon_price): # and (eBay_price <= bb_price):
        elected_price = eBay_price
        elected_link = URL_e
    elif (amazon_price <= eBay_price): # and (amazon_price <= bb_price):
        elected_price = amazon_price
        elected_link = URL
    # elif (bb_price <= amazon_price) and (bb_price <= eBay_price):
    #     elected_price = bb_price
    #     elected_link = URL_bb

    print('Here\'s the link to the lowest price. Have fun!')
    print(elected_link)
    print('$' + str(elected_price))