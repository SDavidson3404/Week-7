import requests
from bs4 import BeautifulSoup

# URL of the LiveSport page you want to scrape
url = "https://www.livesport.com/en"  # Replace with the actual URL

# Send a GET request to fetch the page content
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the relevant HTML elements containing scores
    # Adjust the selectors based on the website's structure
    games = soup.find_all('div', class_='game-score')  # Example class name

    for game in games:
        teams = game.find_all('span', class_='team-name')  # Example class name
        scores = game.find_all('span', class_='score')    # Example class name

        if teams and scores:
            team1 = teams[0].text.strip()
            team2 = teams[1].text.strip()
            score1 = scores[0].text.strip()
            score2 = scores[1].text.strip()

            print(f"{team1} {score1} - {score2} {team2}")
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")
