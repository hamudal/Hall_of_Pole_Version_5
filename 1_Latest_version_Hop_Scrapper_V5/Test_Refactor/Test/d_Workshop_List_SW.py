import requests
from bs4 import BeautifulSoup
import pandas as pd

# Globale Konstante für die Basis-URL
BASE_URL = "https://www.eversports.de"

def scrape_workshops(url):
    """
    Scraped Workshop-Informationen von einer gegebenen URL.

    Args:
        url (str): Die URL der Workshop-Seite.

    Returns:
        DataFrame: Ein DataFrame mit Informationen zu den Workshops.
    """
    response = requests.get(url)
    if response.status_code != 200:
        print("Fehler beim Abrufen der Webseite")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')

    # Listen zur Speicherung der Workshop-Informationen
    workshop_data = {
        'Workshop Name': [],
        'Workshop Date': [],
        'Workshop Price': [],
        'Workshop Units': [],
        'Workshop Studio': [],
        'Workshop Address': [],
        'Workshop Href': []
    }

    # Workshop-Elemente finden
    workshop_elements = soup.find_all('a', class_='marketplace-tile js_marketplace-tile')

    # Durch die Elemente iterieren und Informationen extrahieren
    for workshop in workshop_elements:
        workshop_data['Workshop Name'].append(workshop.find('h4').text)
        workshop_data['Workshop Date'].append(workshop.find('div', class_='marketplace-tile__date').text)
        workshop_data['Workshop Price'].append(workshop.find('div', class_='marketplace-tile__price').text)
        workshop_data['Workshop Units'].append(workshop.find('small', class_='u-text-bold').text)
        
        workshop_content = workshop.find('div', class_='marketplace-tile__content__bottom').find_all('small')
        workshop_data['Workshop Studio'].append(workshop_content[0].text)
        workshop_data['Workshop Address'].append(workshop_content[1].text)
        
        workshop_data['Workshop Href'].append(workshop['href'])

    # DataFrame erstellen und URLs rekonstruieren
    workshoplist_df = pd.DataFrame(workshop_data)
    workshoplist_df['URL_SW'] = BASE_URL + workshoplist_df['Workshop Href']
    workshoplist_df.drop(columns=['Workshop Href'], inplace=True)

    return workshoplist_df

# Beispielaufruf der Funktion
# url = "https://www.eversports.de/sw/poda-studio"
# df = scrape_workshops(url)
# print(df)
