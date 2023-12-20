import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def scrape_workshop_details(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Fehler beim Abrufen der Webseite")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')

    # Extraktion der verschiedenen Datenpunkte
    workshop_name = soup.find('h1', class_='MuiTypography-root MuiTypography-h1 css-1bvkaia').text

    description_div = soup.find('div', class_='css-3awvdx')
    description = ' '.join([p.text for p in description_div.find_all('p')])

    studio_name = soup.find('p', class_='MuiTypography-root MuiTypography-body1 css-z923os').text

    location = soup.find_all('p', class_='MuiTypography-root MuiTypography-body1 css-bjhn26')[2].text

    level = soup.find('p', class_='MuiTypography-root MuiTypography-body1 css-ilcg2f').text

    date = soup.find('p', class_='MuiTypography-root MuiTypography-body1 css-16ai5j1').text

    time = soup.find('p', class_='MuiTypography-root MuiTypography-body1 css-bjhn26').text

    # Weitere Extraktionen (Dauer, Trainer-Infos, Preis, etc.)
    # ...
    
    # Erstellen des DataFrame
    workshop_df = pd.DataFrame({
        'Workshop Name': [workshop_name],
        'Beschreibung': [description],
        'Studio Name': [studio_name],
        'Location': [location],
        'Category': [level],
        'Date': [date],
        'URL_SW': url,
        'Time': time
    })

    return workshop_df

# Beispielaufruf der Funktion
# url = "https://www.eversports.de/e/workshop/mT-MZa2"
# workshop_df = scrape_workshop_details(url)
# print(workshop_df)
