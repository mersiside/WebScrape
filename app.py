import requests
import csv
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# Find all the books in the page
books = soup.find_all('article', {'class': 'product_pod'})

# Write the scraped data to a CSV file
with open('books.csv', mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Price', 'Link'])

    for book in books:
        title = book.h3.a.attrs['title']
        price = book.select('.price_color')[0].get_text()
        link = url + book.h3.a.attrs['href']
        writer.writerow([title, price, link])
