import requests
from bs4 import BeautifulSoup

# URL of NBC News
url = "https://www.nbcnews.com/"

# Send a GET request to fetch the HTML content
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Extract article titles
titles = soup.find_all("h2")  # Adjust the tag based on NBC's HTML structure

# Print the titles
for title in titles:
    print(title.get_text(strip=True))
