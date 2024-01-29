import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging
from urllib.parse import urljoin

# Konfiguration des Logging-Systems
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def scrape_classes(urls):
    """
    Scraped Informationen zu Klassen von einer Liste von URLs.
    """
    base_url = "https://www.eversports.de/e/class/"
    sessions = []

    session = requests.Session()

    for url in urls:
        try:
            response = session.get(url)
            response.raise_for_status()
        except requests.RequestException as e:
            logging.error(f"Fehler beim Abrufen der Webseite {url}: {e}")
            continue

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

# if __name__ == "__main__":
#     test_urls = ["https://www.eversports.de/scl/poda-studio"]
#     klassenlist_df = scrape_classes(test_urls)
#     if klassenlist_df is not None:
#         logging.info(f"Gescrapte Klassen-Daten:\n{klassenlist_df}")
#     else:
#         logging.info("Keine Klassen gescraped.")
