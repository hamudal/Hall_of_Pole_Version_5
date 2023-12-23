from a_URLS_Reconstruction import reconstruct_urls_and_extract_buttons
from b_URLS_Validation import validate_urls
from c_PoleStudio_Overview_S import scrape_pole_studio
from d_Workshop_List_SW import scrape_workshops
from e_Workshop_Overview_E import scrape_workshop_details
from f_Klassen_List_SCL import scrape_classes
from g_Klassen_Overview_E_SCL import scrape_class_details
import pandas as pd


def process_urls(urls):
    """
    Prozessiert eine Liste von URLs durch verschiedene Scraping-Funktionen.
    """
    print("Starte URL-Rekonstruktion...")
    reconstructed_urls_list = [reconstruct_urls_and_extract_buttons(url)[1] for url in urls]
    reconstructed_urls = {k: v for d in reconstructed_urls_list for k, v in d.items()}

    print("Konvertiere in DataFrame...")
    reconstructed_urls_df = pd.DataFrame(list(reconstructed_urls.items()), columns=['Kategorie', 'URL'])
    
    print("Validiere URLs...")
    validated_urls_df = validate_urls(reconstructed_urls_df["URL"].to_list())
    validated_urls = validated_urls_df["Valid_URL"].tolist()

    # Aufteilung und Verarbeitung der URLs
    results = {}
    for url in validated_urls:
        if "/s/" in url:
            print(f"Scrape Pole Studio Daten von {url}...")
            results['pole_studio_data'] = scrape_pole_studio(url)
        elif "/sw/" in url:
            print(f"Scrape Workshops Daten von {url}...")
            results['workshops_data'] = scrape_workshops(url)
        elif "/e/workshop/" in url:
            print(f"Scrape Workshop Details von {url}...")
            results['workshop_details'] = scrape_workshop_details(url)
        elif "/scl/" in url:
            print(f"Scrape Klassen Daten von {url}...")
            classes_data = scrape_classes([url])
            results['classes_data'] = classes_data

            # Prüfen, ob die Spalte 'URL_SCL_E' vorhanden ist
            if 'URL_SCL_E' in classes_data.columns:
                print(f"Scrape Klassen Details von URLs in 'URL_SCL_E'...")
                classes_details_list = []
                for url_scl_e in classes_data['URL_SCL_E'].tolist():
                    class_detail = scrape_class_details(url_scl_e)
                    if class_detail is not None:
                        classes_details_list.append(class_detail)
                if classes_details_list:
                    results['classes_details'] = pd.concat(classes_details_list, ignore_index=True)
    
    print("Verarbeitung abgeschlossen.")
    return results


