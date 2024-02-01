import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging

# Konfiguration des Logging-Systems
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

BASE_URL = "https://www.eversports.de"

def scrape_workshops(url):
    """
    Scraped Workshop-Informationen von einer gegebenen URL.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        logging.error(f"Fehler beim Abrufen der Webseite {url}: {e}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')
    workshop_data = {
        'Workshop Name': [],
        'Workshop Date': [],
        'Workshop Price': [],
        'Workshop Units': [],
        'Workshop Studio': [],
        'Workshop Address': [],
        'Workshop Href': []
    }

    workshop_elements = soup.find_all('a', class_='marketplace-tile js_marketplace-tile')
    for workshop in workshop_elements:
        workshop_data['Workshop Name'].append(workshop.find('h4').text)
        workshop_data['Workshop Date'].append(workshop.find('div', class_='marketplace-tile__date').text)
        workshop_data['Workshop Price'].append(workshop.find('div', class_='marketplace-tile__price').text)
        workshop_data['Workshop Units'].append(workshop.find('small', class_='u-text-bold').text)
        
        workshop_content = workshop.find('div', class_='marketplace-tile__content__bottom').find_all('small')
        workshop_data['Workshop Studio'].append(workshop_content[0].text)
        workshop_data['Workshop Address'].append(workshop_content[1].text)
        
        workshop_data['Workshop Href'].append(BASE_URL + workshop['href'])

    workshoplist_df = pd.DataFrame(workshop_data)
    workshoplist_df.drop(columns=['Workshop Href'], inplace=True)

    return workshoplist_df

# if __name__ == "__main__":
#     test_url = "https://www.eversports.de/sw/poda-studio"
#     df = scrape_workshops(test_url)
#     if df is not None:
#         logging.info(f"Gescrapte Workshop-Daten:\n{df}")
#     else:
#         logging.info("Keine Daten gescraped.")
