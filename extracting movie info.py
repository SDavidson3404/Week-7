import requests
from bs4 import BeautifulSoup

# URL of the IMDb page
url = "https://www.imdb.com/title/tt1375666/"  # Example: Inception

# Send a GET request
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract movie title
title = soup.find('h1').text.strip()

# Extract movie rating
rating = soup.find('span', itemprop='ratingValue').text

# Print the extracted data
print(f"Title: {title}")
print(f"Rating: {rating}")
