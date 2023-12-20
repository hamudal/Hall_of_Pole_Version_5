import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

def scrape_classes(urls):
    base_url = "https://www.eversports.de/e/class/"
    sessions = []

    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        workshop_elements = soup.find_all('li', class_='calendar__slot-bookable')
        for workshop_element in workshop_elements:
            session_short_id = workshop_element.get('data-session-short-id')
            session_time = workshop_element.find('div', class_='session-time').text.strip()
            session_name = workshop_element.find('div', class_='session-name').text.strip()
            available_slots = workshop_element.find('div', class_='ellipsis').text.strip()
            
            trainer_element = workshop_element.find('div', class_='ellipsis')
            trainer = trainer_element.find_next('div', class_='ellipsis').text.strip() if trainer_element else "0"
            
            room_element = workshop_element.find('div', class_='ellipsis')
            room = room_element.find_next('div', class_='ellipsis').find_next('div', class_='ellipsis').text.strip() if room_element else "0"

            workshop_info = {
                'URL_SCL': urljoin(base_url, session_short_id),
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
# urls = ["https://www.eversports.de/scl/poda-studio"]
# klassenlist_df = scrape_classes(urls)
# print(klassenlist_df)
