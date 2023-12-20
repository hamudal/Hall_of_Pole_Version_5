import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd

def scrape_pole_studio(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Fehler beim Abrufen der Webseite")
        return None

    polestudio_soup = BeautifulSoup(response.content, 'html.parser')
    overviewbuttons = extract_overview_buttons(polestudio_soup)
    pole_studio_name = extract_pole_studio_name(polestudio_soup)
    contact_info = extract_contact_info(polestudio_soup)
    address, town, postal_code, street = extract_address(polestudio_soup)
    description_text = extract_description(polestudio_soup)
    rating, num_reviews = extract_rating(polestudio_soup)
    combined_items = extract_rating_factors(polestudio_soup)
    arten = extract_art(polestudio_soup)
    sale = extract_sale(polestudio_soup)
    image_urls = extract_image_urls(polestudio_soup)

    # Erstellen des Dictionaries und Rückgabe als DataFrame
    pole_studio_overview = {
        'PoleStudio_Name': pole_studio_name,
        'Adresse': address,
        'PLZ': postal_code,
        'Stadt': town,
        'Straße': street,
        'Buttons': overviewbuttons,
        'Pole Studio Beschreibung': description_text,
        'Ratingscore': rating,
        'Reviewanzahl': num_reviews,
        'Rating Faktoren': combined_items,
        'E-Mail': contact_info['E-Mail'],
        'Homepage': contact_info['Homepage'],
        'Telefon': contact_info['Telefon'],
        'Eversports Pole Studio Seite': url,
        'Art': arten,
        'Angebot': sale,
        'Bildergalerie': image_urls
    }

    pole_studio_df = pd.DataFrame([pole_studio_overview])
    pole_studio_df['Created Date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pole_studio_df['Updated Date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return pole_studio_df

# Funktionen für spezifische Extraktionen
def extract_overview_buttons(soup):
    buttons = soup.find_all('div', class_="MuiStack-root css-sgccrm")
    return [button.text for div in buttons for button in div.find_all('a')]

def extract_pole_studio_name(soup):
    return soup.find('h1', class_='MuiTypography-root MuiTypography-h1 css-qinhw0').text

def extract_contact_info(soup):
    contact_divs = soup.find_all('div', class_='css-1x2phcg')
    contact_info = {'E-Mail': None, 'Homepage': None, 'Telefon': None}
    for div in contact_divs:
        for a in div.find_all('a', href=True):
            href = a['href']
            if href.startswith('mailto:'):
                contact_info["E-Mail"] = href.replace('mailto:', '')
            elif href.startswith('tel:'):
                contact_info["Telefon"] = href.replace('tel:', '')
            else:
                contact_info["Homepage"] = href
    return contact_info

def extract_address(soup):
    address_element = soup.find('p', class_='MuiTypography-root MuiTypography-body1 css-1619old')
    if address_element:
        address_text = address_element.text.split(',')
        return address_text, address_text[1].split(" ")[2], address_text[1].split(" ")[1], address_text[0]
    return None, None, None, None

def extract_description(soup):
    return soup.find('div', class_="MuiBox-root css-0").text

def extract_rating(soup):
    rating_element = soup.find('p', class_='MuiTypography-root MuiTypography-body1 css-2g7rhg')
    if rating_element:
        parts = rating_element.text.split('(')
        return parts[0].strip(), parts[1].replace(')', '').strip()
    return None, None

def extract_rating_factors(soup):
    items = soup.find_all('div', class_='MuiStack-root css-95g4uk')
    return [f"{item.find('p', class_='MuiTypography-root MuiTypography-body1 css-1k55edk').text}: {item.find('p', class_='MuiTypography-root MuiTypography-body1 css-1y0caop').text}" for item in items if item.find('p', class_='MuiTypography-root MuiTypography-body1 css-1k55edk') and item.find('p', class_='MuiTypography-root MuiTypography-body1 css-1y0caop')]

def extract_art(soup):
    art_elements = soup.find_all("p", class_="MuiTypography-root MuiTypography-body1 css-6ik050")
    return [art.text for art in art_elements]

def extract_sale(soup):
    return soup.find("p", class_="MuiTypography-root MuiTypography-body1 css-153qxhx").text

def extract_image_urls(soup):
    pictures = soup.find_all("div", class_="MuiBox-root css-1fivxf")
    return [img["src"] for div in pictures if (img := div.find("img")) and img.has_attr("src")]

# # Verwenden der Hauptfunktion
# url = "https://www.eversports.de/s/poda-studio"
# pole_studio_df = scrape_pole_studio(url)
# print(pole_studio_df)
