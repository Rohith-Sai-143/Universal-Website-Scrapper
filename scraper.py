import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    # Send an HTTP GET request to fetch the website content
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract all the text content from the parsed HTML
    text_content = soup.get_text()

    return text_content
