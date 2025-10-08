import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = "https://www.azquotes.com/"

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Find quotes on the page (adjust the selector based on the website's structure)
quotes = soup.find_all('a', class_='title')  # Example class; inspect the website for the correct one

# Extract and print the quotes
for quote in quotes:
    print(quote.text.strip())
