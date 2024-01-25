import requests
from bs4 import BeautifulSoup

def get_response_content(url):
    """ Retrieves the content of a webpage via an HTTP request. """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except requests.RequestException as e:
        print(f"Error during HTTP request: {e}")
        return None

def reconstruct_urls_and_extract_buttons(url):
    """
    Reconstructs URLs and extracts buttons for a given URL.

    Args:
        url (str): The URL of the webpage to scrape.

    Returns:
        tuple: A list of link texts and a dictionary of reconstructed URLs.
    """
    content = get_response_content(url)
    if content is None:
        return [], {}

    soup = BeautifulSoup(content, 'html.parser')
    overview_buttons = soup.find_all('div', class_="MuiStack-root css-sgccrm")

    button_url_mapping = {
        'Übersicht': 's',
        'Klassen': 'scl',
        'Workshops': 'sw',
        'Videos': 's',
        'Preise': 'sp',
        'Team': 's'
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
                if text in ['Videos', 'Team']:
                    # Keep the structure for 'Videos' and 'Team' URLs
                    reconstructed_url = f"{url}/{text.lower()}"
                elif text in button_url_mapping:
                    # Ensure precise reconstruction for recognized button texts
                    reconstructed_url = f"https://www.eversports.de/{button_url_mapping[text]}/{dynamic_part}"
                else:
                    # Handling unrecognized text
                    reconstructed_url = f"{url}/{text.lower().replace(' ', '-')}"
                reconstructed_urls[text] = reconstructed_url

    return link_text, reconstructed_urls

# Example call of the function
url = "https://www.eversports.de/s/poda-studio"
link_text, reconstructed_urls = reconstruct_urls_and_extract_buttons(url)
print(link_text, reconstructed_urls)
