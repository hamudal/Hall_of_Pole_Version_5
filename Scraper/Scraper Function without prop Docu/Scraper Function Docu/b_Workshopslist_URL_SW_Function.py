import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_workshops(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Fehler beim Abrufen der Webseite")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')

    # Initialize lists to store workshop information
    workshop_names = []
    workshop_dates = []
    workshop_prices = []
    workshop_units = []
    workshop_studios = []
    workshop_addresses = []
    workshop_hrefs = []

    # Base URL for reconstruction
    base_url = "https://www.eversports.de"

    # Find all workshop elements
    workshop_elements = soup.find_all('a', class_='marketplace-tile js_marketplace-tile')

    # Iterate through the found elements and extract the desired information
    for workshop in workshop_elements:
        workshop_name = workshop.find('h4').text
        workshop_names.append(workshop_name)

        workshop_date = workshop.find('div', class_='marketplace-tile__date').text
        workshop_dates.append(workshop_date)

        workshop_price = workshop.find('div', class_='marketplace-tile__price').text
        workshop_prices.append(workshop_price)

        workshop_unit = workshop.find('small', class_='u-text-bold').text
        workshop_units.append(workshop_unit)

        workshop_content = workshop.find('div', class_='marketplace-tile__content__bottom').find_all('small')
        workshop_studio = workshop_content[0].text
        workshop_studios.append(workshop_studio)
        workshop_address = workshop_content[1].text
        workshop_addresses.append(workshop_address)

        workshop_href = workshop['href']
        workshop_hrefs.append(workshop_href)

    # Create DataFrame and add reconstructed URLs
    workshoplist_df = pd.DataFrame({
        'Workshop Name': workshop_names,
        'Workshop Date': workshop_dates,
        'Workshop Price': workshop_prices,
        'Workshop Units': workshop_units,
        'Workshop Studio': workshop_studios,
        'Workshop Address': workshop_addresses,
        'Workshop Href': workshop_hrefs
    })
    workshoplist_df['URL_SW'] = base_url + workshoplist_df['Workshop Href']
    workshoplist_df.drop(columns=['Workshop Href'], inplace=True)

    return workshoplist_df

# Beispielaufruf der Funktion
# url = "https://www.eversports.de/sw/poda-studio"
# df = scrape_workshops(url)
# print(df)
