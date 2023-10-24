import requests
from bs4 import BeautifulSoup
import pandas as pd 

response = None
soup = None

# ENHANCE Gaming Headphone Stand Headset Holder link
url = 'https://www.amazon.com/ENHANCE-Headphone-Customizable-Lighting-Flexible/dp/B07DR59JLP/'


# access Amazon link without logging in using requests
response = requests.get(url)
if response.status_code == 200:
    # print page on success
    print(response.content)
    # print(response.raw)
else:
     print("Request failed with status code:", response.status_code)

print("OK")

#create headers bearing cookie after successful login
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36",
    "Accept-Language": "en-US, en;q=0.5",
    'Cookie': 'session-id=140-6389706-6118921; session-id-time=2082787201l; ubid-main=132-0745565-5512924'
}

# pass headers as argument to get method
response = requests.get(url, headers=headers)
if response.status_code == 200:
    print(response.status_code)
    print(response.text)
else:
    print("Request failed with status code:", response.status_code)


# create Beautiful Soup Object with page
soup = BeautifulSoup(response.content, "html.parser")

# list to store customer review data 
list = []

# extract div elements containing each customer review data
customers = soup.select("div[data-hook='review']")

for i in customers:
    list.append(
        {   # make a dicttionary and add to list 
            'author': i.select_one(".a-profile-name").string,       # customer name
            'review': i.select_one("div[data-hook='review-collapsed'] span"),   # customer review
            'date': i.select("span[data-hook='review-date']")[0].string         # review date
        },
    )

# convert list to CSV using pandas
df = pd.DataFrame(list)
df.to_csv('customers_reviews.csv', index=False)

print("end")