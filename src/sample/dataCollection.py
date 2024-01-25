import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'https://www.example.com'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the links on the page
links = soup.find_all('a')

# Print the links
for link in links:
    print(link.get('href'))
