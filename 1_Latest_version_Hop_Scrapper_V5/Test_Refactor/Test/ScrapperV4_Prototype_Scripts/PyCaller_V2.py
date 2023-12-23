import asyncio
import pandas as pd
import logging
from a_URLS_Reconstruction_V2 import reconstruct_urls_and_extract_buttons
from b_URLS_Validation_V2 import validate_urls
from c_PoleStudio_URL_S_V2 import scrape_pole_studio
from d_Workshop_List_URL_SW_V2 import scrape_workshops
from e_Workshop_URL_E_V2 import scrape_workshop_details
from f_Class_List_URL_SCL_V2 import scrape_classes
from g_Klassen_Overview_E_SCL_V2 import scrape_class_details

# Konfiguration des Logging-Systems
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

async def process_url_async(url):
    """
    Asynchrone Funktion zum Verarbeiten einer einzelnen URL.
    """
    try:
        if "/s/" in url:
            return scrape_pole_studio(url)
        elif "/sw/" in url:
            return scrape_workshops(url)
        elif "/e/workshop/" in url:
            return scrape_workshop_details(url)
        elif "/scl/" in url:
            return scrape_classes([url])
        elif "/e/class/" in url:
            return scrape_class_details(url)
    except Exception as e:
        logging.error(f"Fehler beim Verarbeiten der URL {url}: {e}")
        return pd.DataFrame()  # Leeres DataFrame bei Fehlern

async def process_urls(urls):
    """
    Asynchrones Verarbeiten einer Liste von URLs.
    """
    tasks = [process_url_async(url) for url in urls]
    results = await asyncio.gather(*tasks)
    return pd.concat(results, ignore_index=True)

# def main():
#     try:
#         initial_urls = ["https://www.eversports.de/s/poda-studio"]  # Beispiel-URLs
#         combined_df = asyncio.run(process_urls(initial_urls))

#         if not combined_df.empty:
#             logging.info("Zusammengeführte Ergebnisse:")
#             logging.info(combined_df)
#         else:
#             logging.info("Keine Daten gefunden.")
#     except Exception as e:
#         logging.error(f"Ein Fehler ist im Hauptprogramm aufgetreten: {e}")

# if __name__ == "__main__":
#     main()
