import requests
from bs4 import BeautifulSoup

def reconstruct_urls_and_extract_buttons(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    overviewbuttons = soup.find_all('div', class_="MuiStack-root css-sgccrm")

    button_url_mapping = {
        'Übersicht': 's',
        'Klassen': 'scl',
        'Workshops': 'sw',
        'Videos': 's/videos',
        'Preise': 'sp',
        'Team': 's/team'
    }

    link_text = []
    reconstructed_urls = {}

    for item in overviewbuttons:
        a_elements = item.find_all('a')
        for a in a_elements:
            text = a.text
            link_text.append(text)
            if text in button_url_mapping:
                reconstructed_url = f"https://www.eversports.de/{button_url_mapping[text]}/poda-studio"
                reconstructed_urls[text] = reconstructed_url

    return link_text, reconstructed_urls

# Beispielaufruf der Funktion
# url = "https://www.eversports.de/s/poda-studio"
# link_text, reconstructed_urls = reconstruct_urls_and_extract_buttons(url)
# print(link_text, reconstructed_urls)




### FIX reconstructed_url = f"https://www.eversports.de/{button_url_mapping[text]}/poda-studio"
