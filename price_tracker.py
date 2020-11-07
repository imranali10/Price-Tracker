import json
import requests
from bs4 import BeautifulSoup
headers = {
    "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}


print("----------------------------------------PRICE TRACKER APPLICATION----------------------------------")

while True:
    print("Please choose One option (1 to 4)")

    choice = int(input("(1)-AMAZON |(2)-FLIPKART |(3)-snapdeal| (4)-Exit:"))

    if choice == 1:
        try:
            url = input("Enter Amazon url:")
            content = requests.get(url, headers=headers)
            soup = BeautifulSoup(content.text, 'lxml')
            price = soup.find(id="priceblock_dealprice").get_text(strip=True)
            title = soup.find(id="productTitle").get_text(strip=True)
            print("Title:", title)
            print("Price:", price)
        except:
            print("Error:invalid url:")

    elif choice == 2:
        try:
            url = input("Enter Flipkart url:")
            content = requests.get(url, headers=headers)
            soup = BeautifulSoup(content.text, 'lxml')
            price = soup.select("._3qQ9m1")[0].get_text()
            title = soup.select("._35KyD6")[0].get_text(strip=True)
            print("Title:", title)
            print("Price:", price)
        except:
            print("Error:invalid url:")

    elif choice == 3:
        try:
            url = input("Enter Snapedeal url:")
            content = requests.get(url, headers=headers)
            soup = BeautifulSoup(content.text, 'lxml')
            title = soup.select(".col-xs-22")[0].get_text(strip=True)
            price = soup.select(".payBlkBig")[0].get_text(strip=True)
            print("Title:", title)
            print("Price:", price)
        except:
            print("Error:invalid url:")
    elif choice == 4:
        print("Thank You!!")
        break

    else:
        print("Please enter the Valid choice:")

    print("---------------------------------------------------------------------------------------")
