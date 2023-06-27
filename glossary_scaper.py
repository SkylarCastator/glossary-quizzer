import requests
from bs4 import BeautifulSoup
import json

def scrape_glossary_terms(url):
    # Send a GET request to the Wikipedia page
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    parser_output = soup.find('div', {'class': 'mw-parser-output'})

    terms = []
    # Extract the glossary terms and their descriptions
    for item in parser_output.find_all('dt'):
        term = item.text.strip()
        definition = item.find_next('dd').text.strip()
        terms.append({'term': term, 'definition': definition})

    return terms

