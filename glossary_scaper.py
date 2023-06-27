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

# URL of the Wikipedia page
url = 'https://en.wikipedia.org/wiki/Glossary_of_computer_science'

# Scrape the glossary terms
glossary_terms = scrape_glossary_terms(url)

# Save the glossary terms as a JSON file
with open('glossary_data/cs_glossary.json', 'w') as json_file:
    json.dump({'glossary': glossary_terms}, json_file, indent=4)