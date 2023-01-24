import requests
# scraping tool
from bs4 import BeautifulSoup

# request to website
req = requests.get('https://www.codewithtomi.com/')

# scraping website content
soup = BeautifulSoup(req.content, 'html.parser')

# filter scraped data
data = soup.find_all('h2', class_='post-title')

for d in data:
    print(d.text)