import requests
import json
import pprint
# url = "https://newsapi.org/v2/top-headlines/sources?apiKey="
category = input("Enter a category in which you want the newspaper like Business, general, technology... :) ")

API_KEY = "03cf57f6ee9141a9871a4537c958a6cd"

url = f"https://newsapi.org/v2/top-headlines/sources?category={category}&apiKey={API_KEY}"
res = requests.get(url)

# pretty = json.dumps(res.json(), indent=2)
news = json.loads(res.text)
# print(news, type(news))

for source in news["sources"]:
    print(source["name"])
    print(source["description"])
    print("-----------------------------")

# pprint.pprint(pretty)

# print(res.json())