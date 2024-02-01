import requests
import pandas as pd
import logging
from concurrent.futures import ThreadPoolExecutor

# Konfiguration des Logging-Systems
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def is_url_valid(url):
    """
    Überprüft, ob eine URL gültig ist.

    Args:
        url (str): Die zu überprüfende URL.

    Returns:
        bool: True, wenn die URL gültig ist, sonst False.
    """
    try:
        response = requests.head(url, allow_redirects=True)
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        logging.error(f"Fehler beim Überprüfen der URL {url}: {e}")
        return False

def validate_urls(url_list):
    """
    Überprüft eine Liste von URLs auf Gültigkeit.

    Args:
        url_list (list): Eine Liste von URLs zur Überprüfung.

    Returns:
        DataFrame: Ein Pandas DataFrame mit gültigen URLs.
    """
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(is_url_valid, url_list))

    valid_urls = [url for url, is_valid in zip(url_list, results) if is_valid]
    valid_urls_df = pd.DataFrame(valid_urls, columns=["Valid_URL"])
    return valid_urls_df

# Beispielaufruf der Funktion
# if __name__ == "__main__":
#     test_url_list = ["https://www.eversports.de/s/poda-studio", "https://invalid-url.com"]
#     valid_urls_df = validate_urls(test_url_list)
#     logging.info(f"Gültige URLs: \n{valid_urls_df}")
