import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging

# Konfiguration des Logging-Systems
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_text_or_none(element):
    """Hilfsfunktion zum sicheren Abrufen des Textes aus einem BeautifulSoup-Element."""
    return element.text if element else None

def scrape_workshop_details(url):
    """
    Scraped detaillierte Informationen eines Workshops von einer gegebenen URL.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        logging.error(f"Fehler beim Abrufen der Webseite {url}: {e}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')

    # Extraktion der verschiedenen Datenpunkte
    workshop_name = get_text_or_none(soup.find('h1', class_='MuiTypography-root MuiTypography-h1 css-1bvkaia'))
    description_div = soup.find('div', class_='css-3awvdx')
    description = ' '.join([p.text for p in description_div.find_all('p')]) if description_div else None
    studio_name = get_text_or_none(soup.find('p', class_='MuiTypography-root MuiTypography-body1 css-z923os'))
    location = get_text_or_none(soup.find_all('p', class_='MuiTypography-root MuiTypography-body1 css-bjhn26')[2])
    level = get_text_or_none(soup.find('p', class_='MuiTypography-root MuiTypography-body1 css-ilcg2f'))
    date = get_text_or_none(soup.find('p', class_='MuiTypography-root MuiTypography-body1 css-16ai5j1'))
    time = get_text_or_none(soup.find('p', class_='MuiTypography-root MuiTypography-body1 css-bjhn26'))

    # Erstellen des DataFrame
    workshop_df = pd.DataFrame({
        'Workshop Name': [workshop_name],
        'Beschreibung': [description],
        'Studio Name': [studio_name],
        'Location': [location],
        'Category': [level],
        'Date': [date],
        'URL_E': [url],
        'Time': [time]
    })

    return workshop_df

# if __name__ == "__main__":
#     test_url = "https://www.eversports.de/e/workshop/mT-MZa2"
#     workshop_df = scrape_workshop_details(test_url)
#     if workshop_df is not None:
#         logging.info(f"Gescrapte Workshop-Details:\n{workshop_df}")
#     else:
#         logging.info("Keine Details gescraped.")
