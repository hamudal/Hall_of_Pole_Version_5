import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

def scrape_classes(urls):
    """
    Scraped Informationen zu Klassen von einer Liste von URLs.

    Args:
        urls (list): Eine Liste von URLs, von denen Klasseninformationen gescraped werden sollen.

    Returns:
        DataFrame: Ein DataFrame mit Informationen zu den Klassen.
    """
    base_url = "https://www.eversports.de/e/class/"
    sessions = []

    session = requests.Session()  # Verwendung einer Session für effizientere Requests

    for url in urls:
        response = session.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        workshop_elements = soup.find_all('li', class_='calendar__slot-bookable')
        for workshop_element in workshop_elements:
            session_short_id = workshop_element.get('data-session-short-id')
            session_time = workshop_element.find('div', class_='session-time').text.strip()
            session_name = workshop_element.find('div', class_='session-name').text.strip()
            available_slots = workshop_element.find('div', class_='ellipsis').text.strip()
            
            trainer_elements = workshop_element.find_all('div', class_='ellipsis')
            trainer = trainer_elements[1].text.strip() if len(trainer_elements) > 1 else "Unbekannt"
            room = trainer_elements[2].text.strip() if len(trainer_elements) > 2 else "Unbekannt"

            workshop_info = {
                'URL_SCL_E': urljoin(base_url, session_short_id),
                'Time': session_time.split(" ● ")[0],
                'Duration': session_time.split(" ● ")[1],
                'Name': session_name,
                'Available Slots': available_slots,
                'Trainer': trainer,
                'Room': room
            }
            sessions.append(workshop_info)

    klassenlist_df = pd.DataFrame(sessions)
    return klassenlist_df

# Beispielaufruf der Funktion
urls = ["https://www.eversports.de/scl/poda-studio"]
klassenlist_df = scrape_classes(urls)
print(klassenlist_df)
