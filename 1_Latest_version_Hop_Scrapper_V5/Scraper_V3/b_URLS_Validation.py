import requests
import pandas as pd
import logging

# Einrichten des Loggings
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
        response = requests.get(url)
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        logging.error(f"Error while checking URL: {url}\nError: {e}")
        return False

def validate_urls(url_list):
    """
    Überprüft eine Liste von URLs auf Gültigkeit.

    Args:
        url_list (list): Eine Liste von URLs zur Überprüfung.

    Returns:
        DataFrame: Ein Pandas DataFrame mit gültigen URLs.
    """
    valid_urls = []
    for index, url in enumerate(url_list):
        logging.info(f"Processing URL {index + 1}/{len(url_list)}: {url}")
        if is_url_valid(url):
            valid_urls.append(url)
            logging.info(f"URL {url} is valid.")
        else:
            logging.info(f"URL {url} is not valid.")

    valid_urls_df = pd.DataFrame(valid_urls, columns=["Valid_URL"])
    valid_urls_df = valid_urls_df.drop_duplicates(subset=['Valid_URL'])
    return valid_urls_df

# Beispielaufruf der Funktion
url_list = ["https://www.eversports.de/s/poda-studio"]
valid_urls_df = validate_urls(url_list)
print(valid_urls_df)
