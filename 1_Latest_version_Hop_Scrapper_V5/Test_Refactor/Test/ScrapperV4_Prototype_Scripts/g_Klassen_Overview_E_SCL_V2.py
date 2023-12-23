import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging
from datetime import datetime

# Konfiguration des Logging-Systems
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_text_or_none(element):
    """Hilfsfunktion zum sicheren Abrufen des Textes aus einem BeautifulSoup-Element."""
    return element.text if element else None

def scrape_class_details(url):
    """
    Scraped detaillierte Informationen einer Klasse von einer gegebenen URL.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        logging.error(f"Fehler beim Abrufen der Webseite {url}: {e}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')

    # Extraktion der verschiedenen Datenpunkte
    class_name = get_text_or_none(soup.find('h1', class_='MuiTypography-root MuiTypography-h1 css-1bvkaia'))
    description_div = soup.find('div', class_='css-3awvdx')
    description = ' '.join([p.text for p in description_div.find_all('p')]) if description_div else None
    studio_name = get_text_or_none(soup.find('p', class_='MuiTypography-root MuiTypography-body1 css-z923os'))
    location = get_text_or_none(soup.find_all('p', class_='MuiTypography-root MuiTypography-body1 css-bjhn26')[2])
    level = get_text_or_none(soup.find('p', class_='MuiTypography-root MuiTypography-body1 css-ilcg2f'))
    date = get_text_or_none(soup.find('p', class_='MuiTypography-root MuiTypography-body1 css-16ai5j1'))
    time = get_text_or_none(soup.find('p', class_='MuiTypography-root MuiTypography-body1 css-bjhn26'))

    class_df = pd.DataFrame({
        'Klassenname': [class_name],
        'Beschreibung': [description],
        'Studio Name': [studio_name],
        'Standort': [location],
        'Kategorie': [level],
        'Datum': [date],
        'URL_E': [url],
        'Zeit': [time]
    })

    return class_df

# if __name__ == "__main__":
#     test_url = "https://www.eversports.de/e/class/mT-MZa2"
#     class_df = scrape_class_details(test_url)
#     if class_df is not None:
#         logging.info(f"Gescrapte Klassen-Details:\n{class_df}")
#     else:
#         logging.info("Keine Klassen-Details gescraped.")
