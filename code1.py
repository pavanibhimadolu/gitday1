import requests
from bs4 import BeautifulSoup
import csv

# URL of the website to scrape
URL = 'http://quotes.toscrape.com/'

# Send a GET request to fetch the page content
response = requests.get(URL)

# Check if the request was successful
if response.status_code == 200:
    print("Successfully fetched the web page!")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
    exit()

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# List to store extracted data
quotes = []

# Extract data (quotes, authors, and tags)
for quote_div in soup.find_all('div', class_='quote'):
    # Extract the quote text
    text = quote_div.find('span', class_='text').text
    
    # Extract the author name
    author = quote_div.find('small', class_='author').text
    
    # Extract the tags (if any)
    tags = [tag.text for tag in quote_div.find_all('a', class_='tag')]
    
    # Append the extracted data to the list
    quotes.append({
        'quote': text,
        'author': author,
        'tags': ', '.join(tags)  # Join tags as a comma-separated string
    })

# Define the CSV file where data will be saved
with open('quotes.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['quote', 'author', 'tags'])
    
    # Write the header row
    writer.writeheader()
    
    # Write all the rows (quotes) to the CSV
    writer.writerows(quotes)

print(f"Scraped data saved to 'quotes.csv'")

