import requests
import pandas as pd

def is_url_valid(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        print(f"Error while checking URL: {url}\nError: {e}")
        return False

def validate_urls(url_list):
    valid_urls = []
    for index, url in enumerate(url_list):
        print(f"Processing URL {index + 1}/{len(url_list)}: {url}")
        if is_url_valid(url):
            valid_urls.append(url)
            print(f"URL {url} is valid.")
        else:
            print(f"URL {url} is not valid.")
        print("\n")
    
    valid_urls_df = pd.DataFrame(valid_urls, columns=["Valid_URL"])
    valid_urls_df = valid_urls_df.drop_duplicates(subset=['Valid_URL'])
    return valid_urls_df

# Beispielaufruf der Funktion
# url_list = ["https://www.eversports.de/s/poda-studio"]
# valid_urls_df = validate_urls(url_list)
# print(valid_urls_df)
