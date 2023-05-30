import requests
from bs4 import BeautifulSoup
# response = requests.get("https://eventor-mern.vercel.app")
# print(response.text)

# url = "https://jsonplaceholder.typicode.com/posts"

# data = {
#     "title": 'Shiv',
#     "body": 'Sahu',
#     "userId": 10,
# }

# headers =  {
#     'Content-type': 'application/json; charset=UTF-8',
#   }

# response = requests.post(url, headers=headers, json=data)

# print(response.text)

url = "https://eventor-mern.vercel.app"

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
for heading in soup.find_all("h2"):
    print(heading.text)