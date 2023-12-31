import requests
from bs4 import BeautifulSoup
import logging

# Konfiguration des Logging-Systems
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_response_content(url):
    """Holt den Inhalt einer Webseite über eine HTTP-Anfrage."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except requests.RequestException as e:
        logging.error(f"Fehler bei der HTTP-Anfrage für {url}: {e}")
        return None

def reconstruct_urls_and_extract_buttons(url):
    """
    Rekonstruiert URLs und extrahiert Buttons für eine gegebene URL.

    Args:
        url (str): Die URL der zu scrapenden Seite.

    Returns:
        tuple: Eine Liste der Link-Texte und ein Dictionary der rekonstruierten URLs.
    """
    content = get_response_content(url)
    if content is None:
        return [], {}

    try:
        soup = BeautifulSoup(content, 'html.parser')
        overview_buttons = soup.find_all('div', class_="MuiStack-root css-sgccrm")

        button_url_mapping = {
            'Übersicht': 's',
            'Klassen': 'scl',
            'Workshops': 'sw',
            'Videos': 's/videos',
            'Preise': 'sp',
            'Team': 's/team'
        }

        dynamic_part = url.split("/")[-1]
        link_text = []
        reconstructed_urls = {}

        if overview_buttons:
            for item in overview_buttons:
                anchor_elements = item.find_all('a')
                for anchor in anchor_elements:
                    text = anchor.text
                    link_text.append(text)
                    if text in button_url_mapping:
                        reconstructed_url = f"https://www.eversports.de/{button_url_mapping[text]}/{dynamic_part}"
                        reconstructed_urls[text] = reconstructed_url

        return link_text, reconstructed_urls

    except Exception as e:
        logging.error(f"Fehler bei der Verarbeitung der URL {url}: {e}")
        return [], {}

# Beispielaufruf der Funktion
# if __name__ == "__main__":
    # test_url = "https://www.eversports.de/s/poda-studio"
    # link_text, reconstructed_urls = reconstruct_urls_and_extract_buttons(test_url)
    # logging.info(f"Link-Texte: {link_text}")
    # logging.info(f"Rekonstruierte URLs: {reconstructed_urls}")