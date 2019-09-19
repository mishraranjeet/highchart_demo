import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
page = requests.get(BASE_URL)
# print(page.text)
parse = BeautifulSoup(page.content, 'html.parser')
for_iphones = parse.find_all('div', {'class': '_3O0U0u'})
# print(len(for_iphone))
# print(BeautifulSoup.prettify(for_iphone[0]))
# prettify brings the html content in structure format
for_iphone = for_iphones[0]
# print(for_iphone.div.img['alt'])

headers = 'ProductName,Price,Ratings,Reviews'
with open('iphone_data.csv', 'w') as file:
    file.write(headers)
    for i in for_iphones:
        product_name = i.div.img['alt']
        product_name = product_name.split('(')[0] + 'series'

        prices = i.find_all('div', {'class': 'col col-5-12 _2o7WAb'})
        price = prices[0].text.strip()
        ratings = i.find_all('div', {'class': "niH0FQ"})
        rating = ratings[0].text
        mrating = rating.split('&')[-2]
        review = rating.split('&')[-1]
        reviews = review.split(' ')[0]
        reviews = ''.join(reviews.split(','))

        tprice = ' '.join(price.split(' '))
        tprice = ''.join(tprice.split(','))
        rprice = tprice.split('₹')
        rs_price = 'Rs ' + rprice[1]
        sprice = rs_price.split('N')
        fprice = sprice[0]

        frating = mrating.split(',')[0]

        print("Product : ", product_name + "\nPrice :", fprice + "\nRating :", frating + "\nReviews :", reviews + "\n")
        file.write("\n" + product_name + ", " + fprice + ", " + frating + "," + reviews + "\n")
